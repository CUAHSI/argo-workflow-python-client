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


class IoArgoprojEventsV1alpha1Service(object):
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
        'cluster_ip': 'str',
        'ports': 'list[IoK8sApiCoreV1ServicePort]'
    }

    attribute_map = {
        'cluster_ip': 'clusterIP',
        'ports': 'ports'
    }

    def __init__(self, cluster_ip=None, ports=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1Service - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster_ip = None
        self._ports = None
        self.discriminator = None

        if cluster_ip is not None:
            self.cluster_ip = cluster_ip
        if ports is not None:
            self.ports = ports

    @property
    def cluster_ip(self):
        """Gets the cluster_ip of this IoArgoprojEventsV1alpha1Service.  # noqa: E501


        :return: The cluster_ip of this IoArgoprojEventsV1alpha1Service.  # noqa: E501
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """Sets the cluster_ip of this IoArgoprojEventsV1alpha1Service.


        :param cluster_ip: The cluster_ip of this IoArgoprojEventsV1alpha1Service.  # noqa: E501
        :type: str
        """

        self._cluster_ip = cluster_ip

    @property
    def ports(self):
        """Gets the ports of this IoArgoprojEventsV1alpha1Service.  # noqa: E501


        :return: The ports of this IoArgoprojEventsV1alpha1Service.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this IoArgoprojEventsV1alpha1Service.


        :param ports: The ports of this IoArgoprojEventsV1alpha1Service.  # noqa: E501
        :type: list[IoK8sApiCoreV1ServicePort]
        """

        self._ports = ports

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
        if issubclass(IoArgoprojEventsV1alpha1Service, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1Service):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1Service):
            return True

        return self.to_dict() != other.to_dict()
