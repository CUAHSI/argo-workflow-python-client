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


class IoArgoprojEventsV1alpha1Int64OrString(object):
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
        'int64_val': 'str',
        'str_val': 'str',
        'type': 'str'
    }

    attribute_map = {
        'int64_val': 'int64Val',
        'str_val': 'strVal',
        'type': 'type'
    }

    def __init__(self, int64_val=None, str_val=None, type=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1Int64OrString - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._int64_val = None
        self._str_val = None
        self._type = None
        self.discriminator = None

        if int64_val is not None:
            self.int64_val = int64_val
        if str_val is not None:
            self.str_val = str_val
        if type is not None:
            self.type = type

    @property
    def int64_val(self):
        """Gets the int64_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501


        :return: The int64_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :rtype: str
        """
        return self._int64_val

    @int64_val.setter
    def int64_val(self, int64_val):
        """Sets the int64_val of this IoArgoprojEventsV1alpha1Int64OrString.


        :param int64_val: The int64_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :type: str
        """

        self._int64_val = int64_val

    @property
    def str_val(self):
        """Gets the str_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501


        :return: The str_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :rtype: str
        """
        return self._str_val

    @str_val.setter
    def str_val(self, str_val):
        """Sets the str_val of this IoArgoprojEventsV1alpha1Int64OrString.


        :param str_val: The str_val of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :type: str
        """

        self._str_val = str_val

    @property
    def type(self):
        """Gets the type of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501


        :return: The type of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoArgoprojEventsV1alpha1Int64OrString.


        :param type: The type of this IoArgoprojEventsV1alpha1Int64OrString.  # noqa: E501
        :type: str
        """

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
        if issubclass(IoArgoprojEventsV1alpha1Int64OrString, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1Int64OrString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1Int64OrString):
            return True

        return self.to_dict() != other.to_dict()