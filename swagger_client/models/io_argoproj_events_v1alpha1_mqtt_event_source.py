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


class IoArgoprojEventsV1alpha1MQTTEventSource(object):
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
        'client_id': 'str',
        'connection_backoff': 'IoArgoprojEventsV1alpha1Backoff',
        'filter': 'IoArgoprojEventsV1alpha1EventSourceFilter',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'tls': 'IoArgoprojEventsV1alpha1TLSConfig',
        'topic': 'str',
        'url': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'connection_backoff': 'connectionBackoff',
        'filter': 'filter',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'tls': 'tls',
        'topic': 'topic',
        'url': 'url'
    }

    def __init__(self, client_id=None, connection_backoff=None, filter=None, json_body=None, metadata=None, tls=None, topic=None, url=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1MQTTEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_id = None
        self._connection_backoff = None
        self._filter = None
        self._json_body = None
        self._metadata = None
        self._tls = None
        self._topic = None
        self._url = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if connection_backoff is not None:
            self.connection_backoff = connection_backoff
        if filter is not None:
            self.filter = filter
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        if tls is not None:
            self.tls = tls
        if topic is not None:
            self.topic = topic
        if url is not None:
            self.url = url

    @property
    def client_id(self):
        """Gets the client_id of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The client_id of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param client_id: The client_id of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def connection_backoff(self):
        """Gets the connection_backoff of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501

        ConnectionBackoff holds backoff applied to connection.  # noqa: E501

        :return: The connection_backoff of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Backoff
        """
        return self._connection_backoff

    @connection_backoff.setter
    def connection_backoff(self, connection_backoff):
        """Sets the connection_backoff of this IoArgoprojEventsV1alpha1MQTTEventSource.

        ConnectionBackoff holds backoff applied to connection.  # noqa: E501

        :param connection_backoff: The connection_backoff of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Backoff
        """

        self._connection_backoff = connection_backoff

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def json_body(self):
        """Gets the json_body of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The json_body of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param json_body: The json_body of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def tls(self):
        """Gets the tls of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The tls of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1TLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param tls: The tls of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1TLSConfig
        """

        self._tls = tls

    @property
    def topic(self):
        """Gets the topic of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The topic of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param topic: The topic of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def url(self):
        """Gets the url of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501


        :return: The url of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojEventsV1alpha1MQTTEventSource.


        :param url: The url of this IoArgoprojEventsV1alpha1MQTTEventSource.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(IoArgoprojEventsV1alpha1MQTTEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1MQTTEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1MQTTEventSource):
            return True

        return self.to_dict() != other.to_dict()
