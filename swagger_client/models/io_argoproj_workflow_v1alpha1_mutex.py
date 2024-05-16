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


class IoArgoprojWorkflowV1alpha1Mutex(object):
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
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, name=None, namespace=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Mutex - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._namespace = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def name(self):
        """Gets the name of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501

        name of the mutex  # noqa: E501

        :return: The name of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojWorkflowV1alpha1Mutex.

        name of the mutex  # noqa: E501

        :param name: The name of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501

        Namespace is the namespace of the mutex, default: [namespace of workflow]  # noqa: E501

        :return: The namespace of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoArgoprojWorkflowV1alpha1Mutex.

        Namespace is the namespace of the mutex, default: [namespace of workflow]  # noqa: E501

        :param namespace: The namespace of this IoArgoprojWorkflowV1alpha1Mutex.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if issubclass(IoArgoprojWorkflowV1alpha1Mutex, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Mutex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Mutex):
            return True

        return self.to_dict() != other.to_dict()
