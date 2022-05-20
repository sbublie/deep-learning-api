from unittest import mock, result
from xml.parsers.expat import model
import tensorflow as tf
import numpy as np
import os
from datetime import datetime

from openapi_server.models.batch import Batch  # noqa: E501
from openapi_server.models.ground_truth_result import GroundTruthResult  # noqa: E501
from openapi_server.models.model import Model  # noqa: E501
from openapi_server.models.model_class import ModelClass  # noqa: E501
from openapi_server.models.prediction_result import PredictionResult  # noqa: E501
from openapi_server.models.status import Status  # noqa: E501
from openapi_server.models.validation_result import ValidationResult  # noqa: E501
from openapi_server import util


class ApiController:
    def __init__(self):

        model_paths = [ f.path for f in os.scandir("./input/model/") if f.is_dir() ]
        batch_paths = [ f.path for f in os.scandir("./input/batch/") if f.is_dir() ]
        
        self.results = []
        self.model_names = []
        self.batch_names = []

        for model_path in model_paths:
            
            model_name = model_path.split('/')[-1]
            model = tf.keras.models.load_model(model_path)
            
            for batch_path in batch_paths:

                batch_name = batch_path.split("/")[-1]
                
                batch_size = 32
                img_height = 224
                img_width = 224

                test_ds = tf.keras.utils.image_dataset_from_directory(
                batch_path,
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size,
                shuffle=False
                )

                # Get information on your classes
                class_names = np.array(test_ds.class_names)

                # Get the ground truth labels
                ground_truth = np.concatenate([y for x, y in test_ds], axis=0)
                # Mapping test labels to the folder names instead of the index
                for i in range(0, len(ground_truth)):
                    ground_truth[i]=int(class_names[ground_truth[i]])

                normalization_layer = tf.keras.layers.Rescaling(1./255)
                test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y)) 
                predictions = model.predict(test_ds)
                predictions = np.argmax(predictions, axis=1)

                self.results.append(ResultWrapper(model_name, batch_name, class_names, predictions, ground_truth))
                self.model_names.append(model_name)
                self.batch_names.append(batch_name)

    
    def _accuracy(self, predictions, ground_truth):
        metric = tf.keras.metrics.Accuracy()
        metric.update_state(predictions, ground_truth)
        return metric.result().numpy()

    def _addBatch(self, batches, batch_name):
        for batch in batches:
            if batch.name == batch_name:
                return
        batches.append(Batch(batch_name))

    def _addModel(self, models, model_name):
        for model in models:
            if model.name == model_name:
                return
        models.append(Model(model_name))

    # --- Methods for API endpoints ---
    def validation_status_get(self):
        warnings = []
        for result in self.results:
            if self._accuracy(result.predictions, result.ground_truth) < 0.40:
                warnings.append(Status(True, "The accuracy of model {} tested with batch {} is below 40 %".format(result.model_name, result.batch_name)))
        return warnings

    def validation_models_get(self):
        models = []
        for result in self.results:
            self._addModel(models, result.model_name)
        return models

    def validation_batches_get(self):
        batches = []
        for result in self.results:
            self._addBatch(batches, result.batch_name)
        return batches

    def validation_models_model_name_get(self, model_name):
        for result in self.results:
            if result.model_name == model_name:
                model_time = datetime.fromtimestamp(int(result.model_name))
                return Model(result.model_name, model_time)
        return 'Not Found', 404
        
    def validation_batches_batch_name_classes_get(self, batch_name):
        for result in self.results:
            if result.batch_name == batch_name:
                return result.classes.tolist()
        return 'Not Found', 404
        
    def validation_models_model_name_batch_name_result_get(self, model_name, batch_name):
        for result in self.results:
            if model_name == result.model_name and batch_name == result.batch_name:
                return ValidationResult(float(self._accuracy(result.predictions, result.ground_truth))*100)
        return 'Not Found', 404

    def validation_models_model_name_batch_name_result_predictions_get(self, model_name, batch_name):
        for result in self.results:
            if model_name == result.model_name and batch_name == result.batch_name:
                return PredictionResult(result.predictions.tolist())
        
    
    def validation_models_model_name_batch_name_result_ground_truth_get(self, model_name, batch_name):
        for result in self.results:
            if model_name == result.model_name and batch_name == result.batch_name:
                return GroundTruthResult(result.ground_truth.tolist())
        return 'Not Found', 404
    
class ResultWrapper:
    def __init__(self, model_name, batch_name, classes, predications, ground_truth) -> None:
        self.model_name = model_name
        self.batch_name = batch_name
        self.classes = classes
        self.predictions = predications
        self.ground_truth = ground_truth

# Create a new instance of ApiController at startup
controller = ApiController()

