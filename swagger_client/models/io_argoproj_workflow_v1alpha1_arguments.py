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


class IoArgoprojWorkflowV1alpha1Arguments(object):
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
        'artifacts': 'list[IoArgoprojWorkflowV1alpha1Artifact]',
        'parameters': 'list[IoArgoprojWorkflowV1alpha1Parameter]'
    }

    attribute_map = {
        'artifacts': 'artifacts',
        'parameters': 'parameters'
    }

    def __init__(self, artifacts=None, parameters=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Arguments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artifacts = None
        self._parameters = None
        self.discriminator = None

        if artifacts is not None:
            self.artifacts = artifacts
        if parameters is not None:
            self.parameters = parameters

    @property
    def artifacts(self):
        """Gets the artifacts of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501

        Artifacts is the list of artifacts to pass to the template or workflow  # noqa: E501

        :return: The artifacts of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501
        :rtype: list[IoArgoprojWorkflowV1alpha1Artifact]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this IoArgoprojWorkflowV1alpha1Arguments.

        Artifacts is the list of artifacts to pass to the template or workflow  # noqa: E501

        :param artifacts: The artifacts of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501
        :type: list[IoArgoprojWorkflowV1alpha1Artifact]
        """

        self._artifacts = artifacts

    @property
    def parameters(self):
        """Gets the parameters of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501

        Parameters is the list of parameters to pass to the template or workflow  # noqa: E501

        :return: The parameters of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501
        :rtype: list[IoArgoprojWorkflowV1alpha1Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this IoArgoprojWorkflowV1alpha1Arguments.

        Parameters is the list of parameters to pass to the template or workflow  # noqa: E501

        :param parameters: The parameters of this IoArgoprojWorkflowV1alpha1Arguments.  # noqa: E501
        :type: list[IoArgoprojWorkflowV1alpha1Parameter]
        """

        self._parameters = parameters

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
        if issubclass(IoArgoprojWorkflowV1alpha1Arguments, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Arguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Arguments):
            return True

        return self.to_dict() != other.to_dict()
