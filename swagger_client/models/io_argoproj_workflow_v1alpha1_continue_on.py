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


class IoArgoprojWorkflowV1alpha1ContinueOn(object):
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
        'error': 'bool',
        'failed': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'failed': 'failed'
    }

    def __init__(self, error=None, failed=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ContinueOn - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._failed = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if failed is not None:
            self.failed = failed

    @property
    def error(self):
        """Gets the error of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501


        :return: The error of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IoArgoprojWorkflowV1alpha1ContinueOn.


        :param error: The error of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def failed(self):
        """Gets the failed of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501


        :return: The failed of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this IoArgoprojWorkflowV1alpha1ContinueOn.


        :param failed: The failed of this IoArgoprojWorkflowV1alpha1ContinueOn.  # noqa: E501
        :type: bool
        """

        self._failed = failed

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
        if issubclass(IoArgoprojWorkflowV1alpha1ContinueOn, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ContinueOn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ContinueOn):
            return True

        return self.to_dict() != other.to_dict()
