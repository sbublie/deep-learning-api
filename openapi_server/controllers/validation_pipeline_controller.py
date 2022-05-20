import connexion
import six

from openapi_server.models.batch import Batch  # noqa: E501
from openapi_server.models.ground_truth_result import GroundTruthResult  # noqa: E501
from openapi_server.models.model import Model  # noqa: E501
from openapi_server.models.model_class import ModelClass  # noqa: E501
from openapi_server.models.prediction_result import PredictionResult  # noqa: E501
from openapi_server.models.status import Status  # noqa: E501
from openapi_server.models.validation_result import ValidationResult  # noqa: E501
from openapi_server import util

from core.api_controller import controller


def validation_batches_batch_name_classes_get(batch_name):  # noqa: E501
    """validation_batches_batch_name_classes_get

     # noqa: E501

    :param batch_name: Name of batch
    :type batch_name: str

    :rtype: List[ModelClass]
    """
    return controller.validation_batches_batch_name_classes_get(batch_name)


def validation_batches_get():  # noqa: E501
    """validation_batches_get

     # noqa: E501


    :rtype: List[Batch]
    """
    return controller.validation_batches_get()


def validation_models_get():  # noqa: E501
    """validation_models_get

     # noqa: E501


    :rtype: List[Model]
    """
    return controller.validation_models_get()


def validation_models_model_name_batch_name_result_get(model_name, batch_name):  # noqa: E501
    """validation_models_model_name_batch_name_result_get

     # noqa: E501

    :param model_name: Name of model
    :type model_name: str
    :param batch_name: Name of batch
    :type batch_name: str

    :rtype: ValidationResult
    """
    return controller.validation_models_model_name_batch_name_result_get(model_name, batch_name)


def validation_models_model_name_batch_name_result_ground_truth_get(model_name, batch_name):  # noqa: E501
    """validation_models_model_name_batch_name_result_ground_truth_get

     # noqa: E501

    :param model_name: Name of model
    :type model_name: str
    :param batch_name: Name of batch
    :type batch_name: str

    :rtype: List[GroundTruthResult]
    """
    return controller.validation_models_model_name_batch_name_result_ground_truth_get(model_name, batch_name)


def validation_models_model_name_batch_name_result_predictions_get(model_name, batch_name):  # noqa: E501
    """validation_models_model_name_batch_name_result_predictions_get

     # noqa: E501

    :param model_name: Name of model
    :type model_name: str
    :param batch_name: Name of batch
    :type batch_name: str

    :rtype: List[PredictionResult]
    """
    return controller.validation_models_model_name_batch_name_result_predictions_get(model_name, batch_name)


def validation_models_model_name_get(model_name):  # noqa: E501
    """validation_models_model_name_get

     # noqa: E501

    :param model_name: Name of model
    :type model_name: str

    :rtype: Model
    """
    return controller.validation_models_model_name_get(model_name)


def validation_status_get():  # noqa: E501
    """validation_status_get

     # noqa: E501


    :rtype: List[Status]
    """
    return controller.validation_status_get()
