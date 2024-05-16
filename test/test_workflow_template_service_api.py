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
from swagger_client.api.workflow_template_service_api import WorkflowTemplateServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkflowTemplateServiceApi(unittest.TestCase):
    """WorkflowTemplateServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.workflow_template_service_api.WorkflowTemplateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workflow_template_service_create_workflow_template(self):
        """Test case for workflow_template_service_create_workflow_template

        """
        pass

    def test_workflow_template_service_delete_workflow_template(self):
        """Test case for workflow_template_service_delete_workflow_template

        """
        pass

    def test_workflow_template_service_get_workflow_template(self):
        """Test case for workflow_template_service_get_workflow_template

        """
        pass

    def test_workflow_template_service_lint_workflow_template(self):
        """Test case for workflow_template_service_lint_workflow_template

        """
        pass

    def test_workflow_template_service_list_workflow_templates(self):
        """Test case for workflow_template_service_list_workflow_templates

        """
        pass

    def test_workflow_template_service_update_workflow_template(self):
        """Test case for workflow_template_service_update_workflow_template

        """
        pass


if __name__ == '__main__':
    unittest.main()