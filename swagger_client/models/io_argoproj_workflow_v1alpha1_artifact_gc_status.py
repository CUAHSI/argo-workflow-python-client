# coding: utf-8

"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/release-3.5/  # noqa: E501

    OpenAPI spec version: VERSION
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class IoArgoprojWorkflowV1alpha1ArtifactGCStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'artifact_results_by_node': 'dict(str, IoArgoprojWorkflowV1alpha1ArtifactResultNodeStatus)'
    }

    attribute_map = {
        'artifact_results_by_node': 'artifactResultsByNode'
    }

    def __init__(self, artifact_results_by_node=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ArtifactGCStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artifact_results_by_node = None
        self.discriminator = None

        if artifact_results_by_node is not None:
            self.artifact_results_by_node = artifact_results_by_node

    @property
    def artifact_results_by_node(self):
        """Gets the artifact_results_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCStatus.  # noqa: E501

        ArtifactResultsByNode maps Node name to result  # noqa: E501

        :return: The artifact_results_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCStatus.  # noqa: E501
        :rtype: dict(str, IoArgoprojWorkflowV1alpha1ArtifactResultNodeStatus)
        """
        return self._artifact_results_by_node

    @artifact_results_by_node.setter
    def artifact_results_by_node(self, artifact_results_by_node):
        """Sets the artifact_results_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCStatus.

        ArtifactResultsByNode maps Node name to result  # noqa: E501

        :param artifact_results_by_node: The artifact_results_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCStatus.  # noqa: E501
        :type: dict(str, IoArgoprojWorkflowV1alpha1ArtifactResultNodeStatus)
        """

        self._artifact_results_by_node = artifact_results_by_node

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoArgoprojWorkflowV1alpha1ArtifactGCStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ArtifactGCStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ArtifactGCStatus):
            return True

        return self.to_dict() != other.to_dict()
