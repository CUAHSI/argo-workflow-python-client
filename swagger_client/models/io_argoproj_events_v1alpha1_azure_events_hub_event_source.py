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


class IoArgoprojEventsV1alpha1AzureEventsHubEventSource(object):
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
        'filter': 'IoArgoprojEventsV1alpha1EventSourceFilter',
        'fqdn': 'str',
        'hub_name': 'str',
        'metadata': 'dict(str, str)',
        'shared_access_key': 'IoK8sApiCoreV1SecretKeySelector',
        'shared_access_key_name': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'filter': 'filter',
        'fqdn': 'fqdn',
        'hub_name': 'hubName',
        'metadata': 'metadata',
        'shared_access_key': 'sharedAccessKey',
        'shared_access_key_name': 'sharedAccessKeyName'
    }

    def __init__(self, filter=None, fqdn=None, hub_name=None, metadata=None, shared_access_key=None, shared_access_key_name=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1AzureEventsHubEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter = None
        self._fqdn = None
        self._hub_name = None
        self._metadata = None
        self._shared_access_key = None
        self._shared_access_key_name = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if fqdn is not None:
            self.fqdn = fqdn
        if hub_name is not None:
            self.hub_name = hub_name
        if metadata is not None:
            self.metadata = metadata
        if shared_access_key is not None:
            self.shared_access_key = shared_access_key
        if shared_access_key_name is not None:
            self.shared_access_key_name = shared_access_key_name

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def fqdn(self):
        """Gets the fqdn of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The fqdn of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param fqdn: The fqdn of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def hub_name(self):
        """Gets the hub_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The hub_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._hub_name

    @hub_name.setter
    def hub_name(self, hub_name):
        """Sets the hub_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param hub_name: The hub_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: str
        """

        self._hub_name = hub_name

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def shared_access_key(self):
        """Gets the shared_access_key of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The shared_access_key of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._shared_access_key

    @shared_access_key.setter
    def shared_access_key(self, shared_access_key):
        """Sets the shared_access_key of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param shared_access_key: The shared_access_key of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._shared_access_key = shared_access_key

    @property
    def shared_access_key_name(self):
        """Gets the shared_access_key_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501


        :return: The shared_access_key_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._shared_access_key_name

    @shared_access_key_name.setter
    def shared_access_key_name(self, shared_access_key_name):
        """Sets the shared_access_key_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.


        :param shared_access_key_name: The shared_access_key_name of this IoArgoprojEventsV1alpha1AzureEventsHubEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._shared_access_key_name = shared_access_key_name

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
        if issubclass(IoArgoprojEventsV1alpha1AzureEventsHubEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1AzureEventsHubEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1AzureEventsHubEventSource):
            return True

        return self.to_dict() != other.to_dict()
