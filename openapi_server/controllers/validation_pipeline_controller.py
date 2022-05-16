import connexion
import six

from openapi_server.models.batch import Batch  # noqa: E501
from openapi_server.models.model import Model  # noqa: E501
from openapi_server.models.model_class import ModelClass  # noqa: E501
from openapi_server.models.validation_result import ValidationResult  # noqa: E501
from openapi_server import util

from core.api_controller import controller

def validation_batches_batch_id_classes_get():  # noqa: E501
    """validation_batches_batch_id_classes_get

     # noqa: E501


    :rtype: List[ModelClass]
    """
    return 'do some magic!'


def validation_batches_get():  # noqa: E501
    """validation_batches_get

     # noqa: E501


    :rtype: List[Batch]
    """
    return 'do some magic!'


def validation_models_get():  # noqa: E501
    """validation_models_get

     # noqa: E501


    :rtype: List[Model]
    """
    return [Model(controller.model_name, controller.model_name)]


def validation_models_model_id_batch_id_classes_get(model_id, batch_id):  # noqa: E501
    """validation_models_model_id_batch_id_classes_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str
    :param batch_id: ID of batch
    :type batch_id: str

    :rtype: List[ModelClass]
    """
    return 'do some magic!'


def validation_models_model_id_batch_id_ground_truth_get(model_id, batch_id):  # noqa: E501
    """validation_models_model_id_batch_id_ground_truth_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str
    :param batch_id: ID of batch
    :type batch_id: str

    :rtype: ValidationResult
    """
    return 'do some magic!'


def validation_models_model_id_batch_id_predictions_get(model_id, batch_id):  # noqa: E501
    """validation_models_model_id_batch_id_predictions_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str
    :param batch_id: ID of batch
    :type batch_id: str

    :rtype: ValidationResult
    """
    return 'do some magic!'


def validation_models_model_id_batch_id_result_get(model_id, batch_id):  # noqa: E501
    """validation_models_model_id_batch_id_result_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str
    :param batch_id: ID of batch
    :type batch_id: str

    :rtype: ValidationResult
    """
    return 'do some magic!'


def validation_models_model_id_get(model_id):  # noqa: E501
    """validation_models_model_id_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str

    :rtype: Model
    """
    return 'do some magic!'
