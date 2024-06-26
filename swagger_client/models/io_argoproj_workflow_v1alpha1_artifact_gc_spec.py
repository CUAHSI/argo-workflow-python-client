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


class IoArgoprojWorkflowV1alpha1ArtifactGCSpec(object):
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
        'artifacts_by_node': 'dict(str, IoArgoprojWorkflowV1alpha1ArtifactNodeSpec)'
    }

    attribute_map = {
        'artifacts_by_node': 'artifactsByNode'
    }

    def __init__(self, artifacts_by_node=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ArtifactGCSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artifacts_by_node = None
        self.discriminator = None

        if artifacts_by_node is not None:
            self.artifacts_by_node = artifacts_by_node

    @property
    def artifacts_by_node(self):
        """Gets the artifacts_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCSpec.  # noqa: E501

        ArtifactsByNode maps Node name to information pertaining to Artifacts on that Node  # noqa: E501

        :return: The artifacts_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCSpec.  # noqa: E501
        :rtype: dict(str, IoArgoprojWorkflowV1alpha1ArtifactNodeSpec)
        """
        return self._artifacts_by_node

    @artifacts_by_node.setter
    def artifacts_by_node(self, artifacts_by_node):
        """Sets the artifacts_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCSpec.

        ArtifactsByNode maps Node name to information pertaining to Artifacts on that Node  # noqa: E501

        :param artifacts_by_node: The artifacts_by_node of this IoArgoprojWorkflowV1alpha1ArtifactGCSpec.  # noqa: E501
        :type: dict(str, IoArgoprojWorkflowV1alpha1ArtifactNodeSpec)
        """

        self._artifacts_by_node = artifacts_by_node

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
        if issubclass(IoArgoprojWorkflowV1alpha1ArtifactGCSpec, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ArtifactGCSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ArtifactGCSpec):
            return True

        return self.to_dict() != other.to_dict()
