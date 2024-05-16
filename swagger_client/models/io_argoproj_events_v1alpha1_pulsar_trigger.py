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


class IoArgoprojEventsV1alpha1PulsarTrigger(object):
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
        'auth_token_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'connection_backoff': 'IoArgoprojEventsV1alpha1Backoff',
        'parameters': 'list[IoArgoprojEventsV1alpha1TriggerParameter]',
        'payload': 'list[IoArgoprojEventsV1alpha1TriggerParameter]',
        'tls': 'IoArgoprojEventsV1alpha1TLSConfig',
        'tls_allow_insecure_connection': 'bool',
        'tls_trust_certs_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'tls_validate_hostname': 'bool',
        'topic': 'str',
        'url': 'str'
    }

    attribute_map = {
        'auth_token_secret': 'authTokenSecret',
        'connection_backoff': 'connectionBackoff',
        'parameters': 'parameters',
        'payload': 'payload',
        'tls': 'tls',
        'tls_allow_insecure_connection': 'tlsAllowInsecureConnection',
        'tls_trust_certs_secret': 'tlsTrustCertsSecret',
        'tls_validate_hostname': 'tlsValidateHostname',
        'topic': 'topic',
        'url': 'url'
    }

    def __init__(self, auth_token_secret=None, connection_backoff=None, parameters=None, payload=None, tls=None, tls_allow_insecure_connection=None, tls_trust_certs_secret=None, tls_validate_hostname=None, topic=None, url=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1PulsarTrigger - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_token_secret = None
        self._connection_backoff = None
        self._parameters = None
        self._payload = None
        self._tls = None
        self._tls_allow_insecure_connection = None
        self._tls_trust_certs_secret = None
        self._tls_validate_hostname = None
        self._topic = None
        self._url = None
        self.discriminator = None

        if auth_token_secret is not None:
            self.auth_token_secret = auth_token_secret
        if connection_backoff is not None:
            self.connection_backoff = connection_backoff
        if parameters is not None:
            self.parameters = parameters
        if payload is not None:
            self.payload = payload
        if tls is not None:
            self.tls = tls
        if tls_allow_insecure_connection is not None:
            self.tls_allow_insecure_connection = tls_allow_insecure_connection
        if tls_trust_certs_secret is not None:
            self.tls_trust_certs_secret = tls_trust_certs_secret
        if tls_validate_hostname is not None:
            self.tls_validate_hostname = tls_validate_hostname
        if topic is not None:
            self.topic = topic
        if url is not None:
            self.url = url

    @property
    def auth_token_secret(self):
        """Gets the auth_token_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The auth_token_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._auth_token_secret

    @auth_token_secret.setter
    def auth_token_secret(self, auth_token_secret):
        """Sets the auth_token_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param auth_token_secret: The auth_token_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._auth_token_secret = auth_token_secret

    @property
    def connection_backoff(self):
        """Gets the connection_backoff of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The connection_backoff of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Backoff
        """
        return self._connection_backoff

    @connection_backoff.setter
    def connection_backoff(self, connection_backoff):
        """Sets the connection_backoff of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param connection_backoff: The connection_backoff of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Backoff
        """

        self._connection_backoff = connection_backoff

    @property
    def parameters(self):
        """Gets the parameters of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501

        Parameters is the list of parameters that is applied to resolved Kafka trigger object.  # noqa: E501

        :return: The parameters of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this IoArgoprojEventsV1alpha1PulsarTrigger.

        Parameters is the list of parameters that is applied to resolved Kafka trigger object.  # noqa: E501

        :param parameters: The parameters of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """

        self._parameters = parameters

    @property
    def payload(self):
        """Gets the payload of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501

        Payload is the list of key-value extracted from an event payload to construct the request payload.  # noqa: E501

        :return: The payload of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this IoArgoprojEventsV1alpha1PulsarTrigger.

        Payload is the list of key-value extracted from an event payload to construct the request payload.  # noqa: E501

        :param payload: The payload of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """

        self._payload = payload

    @property
    def tls(self):
        """Gets the tls of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The tls of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1TLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param tls: The tls of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1TLSConfig
        """

        self._tls = tls

    @property
    def tls_allow_insecure_connection(self):
        """Gets the tls_allow_insecure_connection of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The tls_allow_insecure_connection of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._tls_allow_insecure_connection

    @tls_allow_insecure_connection.setter
    def tls_allow_insecure_connection(self, tls_allow_insecure_connection):
        """Sets the tls_allow_insecure_connection of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param tls_allow_insecure_connection: The tls_allow_insecure_connection of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: bool
        """

        self._tls_allow_insecure_connection = tls_allow_insecure_connection

    @property
    def tls_trust_certs_secret(self):
        """Gets the tls_trust_certs_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The tls_trust_certs_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._tls_trust_certs_secret

    @tls_trust_certs_secret.setter
    def tls_trust_certs_secret(self, tls_trust_certs_secret):
        """Sets the tls_trust_certs_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param tls_trust_certs_secret: The tls_trust_certs_secret of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._tls_trust_certs_secret = tls_trust_certs_secret

    @property
    def tls_validate_hostname(self):
        """Gets the tls_validate_hostname of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The tls_validate_hostname of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validate_hostname

    @tls_validate_hostname.setter
    def tls_validate_hostname(self, tls_validate_hostname):
        """Sets the tls_validate_hostname of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param tls_validate_hostname: The tls_validate_hostname of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: bool
        """

        self._tls_validate_hostname = tls_validate_hostname

    @property
    def topic(self):
        """Gets the topic of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The topic of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param topic: The topic of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def url(self):
        """Gets the url of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501


        :return: The url of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojEventsV1alpha1PulsarTrigger.


        :param url: The url of this IoArgoprojEventsV1alpha1PulsarTrigger.  # noqa: E501
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
        if issubclass(IoArgoprojEventsV1alpha1PulsarTrigger, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1PulsarTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1PulsarTrigger):
            return True

        return self.to_dict() != other.to_dict()