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


class IoArgoprojEventsV1alpha1EventSource(object):
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
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta',
        'spec': 'IoArgoprojEventsV1alpha1EventSourceSpec',
        'status': 'IoArgoprojEventsV1alpha1EventSourceStatus'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, metadata=None, spec=None, status=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1EventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1EventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501


        :return: The spec of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this IoArgoprojEventsV1alpha1EventSource.


        :param spec: The spec of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceSpec
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501


        :return: The status of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoArgoprojEventsV1alpha1EventSource.


        :param status: The status of this IoArgoprojEventsV1alpha1EventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceStatus
        """

        self._status = status

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
        if issubclass(IoArgoprojEventsV1alpha1EventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1EventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1EventSource):
            return True

        return self.to_dict() != other.to_dict()