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


class IoArgoprojWorkflowV1alpha1Synchronization(object):
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
        'mutex': 'IoArgoprojWorkflowV1alpha1Mutex',
        'semaphore': 'IoArgoprojWorkflowV1alpha1SemaphoreRef'
    }

    attribute_map = {
        'mutex': 'mutex',
        'semaphore': 'semaphore'
    }

    def __init__(self, mutex=None, semaphore=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Synchronization - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mutex = None
        self._semaphore = None
        self.discriminator = None

        if mutex is not None:
            self.mutex = mutex
        if semaphore is not None:
            self.semaphore = semaphore

    @property
    def mutex(self):
        """Gets the mutex of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501

        Mutex holds the Mutex lock details  # noqa: E501

        :return: The mutex of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1Mutex
        """
        return self._mutex

    @mutex.setter
    def mutex(self, mutex):
        """Sets the mutex of this IoArgoprojWorkflowV1alpha1Synchronization.

        Mutex holds the Mutex lock details  # noqa: E501

        :param mutex: The mutex of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1Mutex
        """

        self._mutex = mutex

    @property
    def semaphore(self):
        """Gets the semaphore of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501

        Semaphore holds the Semaphore configuration  # noqa: E501

        :return: The semaphore of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1SemaphoreRef
        """
        return self._semaphore

    @semaphore.setter
    def semaphore(self, semaphore):
        """Sets the semaphore of this IoArgoprojWorkflowV1alpha1Synchronization.

        Semaphore holds the Semaphore configuration  # noqa: E501

        :param semaphore: The semaphore of this IoArgoprojWorkflowV1alpha1Synchronization.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1SemaphoreRef
        """

        self._semaphore = semaphore

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
        if issubclass(IoArgoprojWorkflowV1alpha1Synchronization, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Synchronization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Synchronization):
            return True

        return self.to_dict() != other.to_dict()
