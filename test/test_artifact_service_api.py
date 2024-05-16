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
from swagger_client.api.artifact_service_api import ArtifactServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestArtifactServiceApi(unittest.TestCase):
    """ArtifactServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.artifact_service_api.ArtifactServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_artifact_service_get_artifact_file(self):
        """Test case for artifact_service_get_artifact_file

        Get an artifact.  # noqa: E501
        """
        pass

    def test_artifact_service_get_input_artifact(self):
        """Test case for artifact_service_get_input_artifact

        Get an input artifact.  # noqa: E501
        """
        pass

    def test_artifact_service_get_input_artifact_by_uid(self):
        """Test case for artifact_service_get_input_artifact_by_uid

        Get an input artifact by UID.  # noqa: E501
        """
        pass

    def test_artifact_service_get_output_artifact(self):
        """Test case for artifact_service_get_output_artifact

        Get an output artifact.  # noqa: E501
        """
        pass

    def test_artifact_service_get_output_artifact_by_uid(self):
        """Test case for artifact_service_get_output_artifact_by_uid

        Get an output artifact by UID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()