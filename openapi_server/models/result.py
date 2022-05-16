# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Result(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accuracy=None):  # noqa: E501
        """Result - a model defined in OpenAPI

        :param accuracy: The accuracy of this Result.  # noqa: E501
        :type accuracy: int
        """
        self.openapi_types = {
            'accuracy': int
        }

        self.attribute_map = {
            'accuracy': 'accuracy'
        }

        self._accuracy = accuracy

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accuracy(self):
        """Gets the accuracy of this Result.


        :return: The accuracy of this Result.
        :rtype: int
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """Sets the accuracy of this Result.


        :param accuracy: The accuracy of this Result.
        :type accuracy: int
        """

        self._accuracy = accuracy
