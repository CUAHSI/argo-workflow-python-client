# coding: utf-8

"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/release-3.5/  # noqa: E501

    OpenAPI spec version: VERSION
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.event_service_api import EventServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEventServiceApi(unittest.TestCase):
    """EventServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.event_service_api.EventServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_service_list_workflow_event_bindings(self):
        """Test case for event_service_list_workflow_event_bindings

        """
        pass

    def test_event_service_receive_event(self):
        """Test case for event_service_receive_event

        """
        pass


if __name__ == '__main__':
    unittest.main()
