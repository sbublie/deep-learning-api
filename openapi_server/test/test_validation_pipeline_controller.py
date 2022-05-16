# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.batch import Batch  # noqa: E501
from openapi_server.models.model import Model  # noqa: E501
from openapi_server.models.model_class import ModelClass  # noqa: E501
from openapi_server.models.validation_result import ValidationResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestValidationPipelineController(BaseTestCase):
    """ValidationPipelineController integration test stubs"""

    def test_validation_batches_batch_id_classes_get(self):
        """Test case for validation_batches_batch_id_classes_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/batches/{batch_id}/classes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_batches_get(self):
        """Test case for validation_batches_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/batches',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_model_model_id_batch_id_classes_get(self):
        """Test case for validation_model_model_id_batch_id_classes_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/model/{model_id}/{batch_id}/classes'.format(model_id='model_id_example', batch_id='batch_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_model_model_id_batch_id_ground_truth_get(self):
        """Test case for validation_model_model_id_batch_id_ground_truth_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/model/{model_id}/{batch_id}/ground_truth'.format(model_id='model_id_example', batch_id='batch_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_model_model_id_batch_id_predictions_get(self):
        """Test case for validation_model_model_id_batch_id_predictions_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/model/{model_id}/{batch_id}/predictions'.format(model_id='model_id_example', batch_id='batch_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_model_model_id_batch_id_result_get(self):
        """Test case for validation_model_model_id_batch_id_result_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/model/{model_id}/{batch_id}/result'.format(model_id='model_id_example', batch_id='batch_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_model_model_id_get(self):
        """Test case for validation_model_model_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/model/{model_id}'.format(model_id='model_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validation_models_get(self):
        """Test case for validation_models_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/validation/models',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
