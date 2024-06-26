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


class IoArgoprojWorkflowV1alpha1TTLStrategy(object):
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
        'seconds_after_completion': 'int',
        'seconds_after_failure': 'int',
        'seconds_after_success': 'int'
    }

    attribute_map = {
        'seconds_after_completion': 'secondsAfterCompletion',
        'seconds_after_failure': 'secondsAfterFailure',
        'seconds_after_success': 'secondsAfterSuccess'
    }

    def __init__(self, seconds_after_completion=None, seconds_after_failure=None, seconds_after_success=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1TTLStrategy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._seconds_after_completion = None
        self._seconds_after_failure = None
        self._seconds_after_success = None
        self.discriminator = None

        if seconds_after_completion is not None:
            self.seconds_after_completion = seconds_after_completion
        if seconds_after_failure is not None:
            self.seconds_after_failure = seconds_after_failure
        if seconds_after_success is not None:
            self.seconds_after_success = seconds_after_success

    @property
    def seconds_after_completion(self):
        """Gets the seconds_after_completion of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501

        SecondsAfterCompletion is the number of seconds to live after completion  # noqa: E501

        :return: The seconds_after_completion of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_completion

    @seconds_after_completion.setter
    def seconds_after_completion(self, seconds_after_completion):
        """Sets the seconds_after_completion of this IoArgoprojWorkflowV1alpha1TTLStrategy.

        SecondsAfterCompletion is the number of seconds to live after completion  # noqa: E501

        :param seconds_after_completion: The seconds_after_completion of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_completion = seconds_after_completion

    @property
    def seconds_after_failure(self):
        """Gets the seconds_after_failure of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501

        SecondsAfterFailure is the number of seconds to live after failure  # noqa: E501

        :return: The seconds_after_failure of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_failure

    @seconds_after_failure.setter
    def seconds_after_failure(self, seconds_after_failure):
        """Sets the seconds_after_failure of this IoArgoprojWorkflowV1alpha1TTLStrategy.

        SecondsAfterFailure is the number of seconds to live after failure  # noqa: E501

        :param seconds_after_failure: The seconds_after_failure of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_failure = seconds_after_failure

    @property
    def seconds_after_success(self):
        """Gets the seconds_after_success of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501

        SecondsAfterSuccess is the number of seconds to live after success  # noqa: E501

        :return: The seconds_after_success of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_success

    @seconds_after_success.setter
    def seconds_after_success(self, seconds_after_success):
        """Sets the seconds_after_success of this IoArgoprojWorkflowV1alpha1TTLStrategy.

        SecondsAfterSuccess is the number of seconds to live after success  # noqa: E501

        :param seconds_after_success: The seconds_after_success of this IoArgoprojWorkflowV1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_success = seconds_after_success

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
        if issubclass(IoArgoprojWorkflowV1alpha1TTLStrategy, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1TTLStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1TTLStrategy):
            return True

        return self.to_dict() != other.to_dict()
