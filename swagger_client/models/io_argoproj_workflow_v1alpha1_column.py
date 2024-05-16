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


class IoArgoprojWorkflowV1alpha1Column(object):
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
        'key': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, key=None, name=None, type=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Column - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._name = None
        self._type = None
        self.discriminator = None

        self.key = key
        self.name = name
        self.type = type

    @property
    def key(self):
        """Gets the key of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501

        The key of the label or annotation, e.g., \"workflows.argoproj.io/completed\".  # noqa: E501

        :return: The key of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoArgoprojWorkflowV1alpha1Column.

        The key of the label or annotation, e.g., \"workflows.argoproj.io/completed\".  # noqa: E501

        :param key: The key of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501

        The name of this column, e.g., \"Workflow Completed\".  # noqa: E501

        :return: The name of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojWorkflowV1alpha1Column.

        The name of this column, e.g., \"Workflow Completed\".  # noqa: E501

        :param name: The name of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501

        The type of this column, \"label\" or \"annotation\".  # noqa: E501

        :return: The type of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoArgoprojWorkflowV1alpha1Column.

        The type of this column, \"label\" or \"annotation\".  # noqa: E501

        :param type: The type of this IoArgoprojWorkflowV1alpha1Column.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(IoArgoprojWorkflowV1alpha1Column, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Column):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Column):
            return True

        return self.to_dict() != other.to_dict()