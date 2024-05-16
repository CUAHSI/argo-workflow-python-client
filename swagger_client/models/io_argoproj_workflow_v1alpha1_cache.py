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


class IoArgoprojWorkflowV1alpha1Cache(object):
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
        'config_map': 'IoK8sApiCoreV1ConfigMapKeySelector'
    }

    attribute_map = {
        'config_map': 'configMap'
    }

    def __init__(self, config_map=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Cache - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_map = None
        self.discriminator = None

        self.config_map = config_map

    @property
    def config_map(self):
        """Gets the config_map of this IoArgoprojWorkflowV1alpha1Cache.  # noqa: E501

        ConfigMap sets a ConfigMap-based cache  # noqa: E501

        :return: The config_map of this IoArgoprojWorkflowV1alpha1Cache.  # noqa: E501
        :rtype: IoK8sApiCoreV1ConfigMapKeySelector
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this IoArgoprojWorkflowV1alpha1Cache.

        ConfigMap sets a ConfigMap-based cache  # noqa: E501

        :param config_map: The config_map of this IoArgoprojWorkflowV1alpha1Cache.  # noqa: E501
        :type: IoK8sApiCoreV1ConfigMapKeySelector
        """
        if self._configuration.client_side_validation and config_map is None:
            raise ValueError("Invalid value for `config_map`, must not be `None`")  # noqa: E501

        self._config_map = config_map

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
        if issubclass(IoArgoprojWorkflowV1alpha1Cache, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Cache):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Cache):
            return True

        return self.to_dict() != other.to_dict()