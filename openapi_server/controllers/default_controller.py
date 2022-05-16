import connexion
import six
from core.api_controller import controller

from openapi_server.models.model import Model  # noqa: E501
from openapi_server.models.model_class import ModelClass  # noqa: E501
from openapi_server.models.result import Result  # noqa: E501
from openapi_server import util



def model_model_id_get(model_id):  # noqa: E501
    """model_model_id_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str

    :rtype: Model
    """
    return Model(controller.model_name)


def model_model_id_result_get(model_id):  # noqa: E501
    """model_model_id_result_get

     # noqa: E501

    :param model_id: ID of model
    :type model_id: str

    :rtype: Result
    """
    return Result(str(controller.accuracy(controller.predictions, controller.test_labels)*100))


def models_get():  # noqa: E501
    """models_get

     # noqa: E501


    :rtype: List[ModelClass]
    """
    return [ModelClass(controller.model_name, controller.model_name)]
