import tensorflow as tf
import numpy as np

class ApiController:
    def __init__(self):
        # //////////////////////////////////////// Load model
        self.model_name = "1652208069"
        import_path = "./input/model/{}".format(int(self.model_name))
        model = tf.keras.models.load_model(import_path)

        # //////////////////////////////////////// Load data
        # You will need to unzip the respective batch folders.
        # Obviously Batch_0 is not sufficient for testing as you will soon find out.
        data_root = "./input/batch/Batch_0/"
        batch_size = 32
        img_height = 224
        img_width = 224

        test_ds = tf.keras.utils.image_dataset_from_directory(
        data_root,
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        shuffle=False
        )

        # # Get information on your classes
        class_names = np.array(test_ds.class_names)
        #print('Classes available: ', class_names)

        # # get the ground truth labels
        self.test_labels = np.concatenate([y for x, y in test_ds], axis=0)
        # # Mapping test labels to the folder names instead of the index
        for i in range(0, len(self.test_labels)):
            self.test_labels[i]=int(class_names[self.test_labels[i]])

        # # Remember that we had some preprocessing before our training this needs to be repeated here
        # # Preprocessing as the tensorflow hub models expect images as float inputs [0,1]
        normalization_layer = tf.keras.layers.Rescaling(1./255)
        test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))  # Where x—images, y—labels.


        # # //////////////////////////////////////// Inference.
        self.predictions = model.predict(test_ds)
        self.predictions = np.argmax(self.predictions, axis=1)
        #print('Predictions: ', self.predictions)
        #print('Ground truth: ', self.test_labels)


        # # //////////////////////////////////////// Let the validation begin
        # # Probably you will want to at least migrate these to another script or class when this grows..
    def accuracy(self, predictions, test_labels):
        metric = tf.keras.metrics.Accuracy()
        metric.update_state(predictions, test_labels)
        return metric.result().numpy()




controller = ApiController()

