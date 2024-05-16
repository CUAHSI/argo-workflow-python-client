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


class IoArgoprojEventsV1alpha1OwnedRepositories(object):
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
        'names': 'list[str]',
        'owner': 'str'
    }

    attribute_map = {
        'names': 'names',
        'owner': 'owner'
    }

    def __init__(self, names=None, owner=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1OwnedRepositories - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._names = None
        self._owner = None
        self.discriminator = None

        if names is not None:
            self.names = names
        if owner is not None:
            self.owner = owner

    @property
    def names(self):
        """Gets the names of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501


        :return: The names of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this IoArgoprojEventsV1alpha1OwnedRepositories.


        :param names: The names of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def owner(self):
        """Gets the owner of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501


        :return: The owner of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IoArgoprojEventsV1alpha1OwnedRepositories.


        :param owner: The owner of this IoArgoprojEventsV1alpha1OwnedRepositories.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if issubclass(IoArgoprojEventsV1alpha1OwnedRepositories, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1OwnedRepositories):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1OwnedRepositories):
            return True

        return self.to_dict() != other.to_dict()
