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


class IoArgoprojEventsV1alpha1WebhookContext(object):
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
        'auth_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'endpoint': 'str',
        'max_payload_size': 'str',
        'metadata': 'dict(str, str)',
        'method': 'str',
        'port': 'str',
        'server_cert_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'server_key_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'url': 'str'
    }

    attribute_map = {
        'auth_secret': 'authSecret',
        'endpoint': 'endpoint',
        'max_payload_size': 'maxPayloadSize',
        'metadata': 'metadata',
        'method': 'method',
        'port': 'port',
        'server_cert_secret': 'serverCertSecret',
        'server_key_secret': 'serverKeySecret',
        'url': 'url'
    }

    def __init__(self, auth_secret=None, endpoint=None, max_payload_size=None, metadata=None, method=None, port=None, server_cert_secret=None, server_key_secret=None, url=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1WebhookContext - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_secret = None
        self._endpoint = None
        self._max_payload_size = None
        self._metadata = None
        self._method = None
        self._port = None
        self._server_cert_secret = None
        self._server_key_secret = None
        self._url = None
        self.discriminator = None

        if auth_secret is not None:
            self.auth_secret = auth_secret
        if endpoint is not None:
            self.endpoint = endpoint
        if max_payload_size is not None:
            self.max_payload_size = max_payload_size
        if metadata is not None:
            self.metadata = metadata
        if method is not None:
            self.method = method
        if port is not None:
            self.port = port
        if server_cert_secret is not None:
            self.server_cert_secret = server_cert_secret
        if server_key_secret is not None:
            self.server_key_secret = server_key_secret
        if url is not None:
            self.url = url

    @property
    def auth_secret(self):
        """Gets the auth_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The auth_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._auth_secret

    @auth_secret.setter
    def auth_secret(self, auth_secret):
        """Sets the auth_secret of this IoArgoprojEventsV1alpha1WebhookContext.


        :param auth_secret: The auth_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._auth_secret = auth_secret

    @property
    def endpoint(self):
        """Gets the endpoint of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The endpoint of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this IoArgoprojEventsV1alpha1WebhookContext.


        :param endpoint: The endpoint of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def max_payload_size(self):
        """Gets the max_payload_size of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The max_payload_size of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: str
        """
        return self._max_payload_size

    @max_payload_size.setter
    def max_payload_size(self, max_payload_size):
        """Sets the max_payload_size of this IoArgoprojEventsV1alpha1WebhookContext.


        :param max_payload_size: The max_payload_size of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: str
        """

        self._max_payload_size = max_payload_size

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1WebhookContext.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def method(self):
        """Gets the method of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The method of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this IoArgoprojEventsV1alpha1WebhookContext.


        :param method: The method of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def port(self):
        """Gets the port of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501

        Port on which HTTP server is listening for incoming events.  # noqa: E501

        :return: The port of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IoArgoprojEventsV1alpha1WebhookContext.

        Port on which HTTP server is listening for incoming events.  # noqa: E501

        :param port: The port of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def server_cert_secret(self):
        """Gets the server_cert_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501

        ServerCertPath refers the file that contains the cert.  # noqa: E501

        :return: The server_cert_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._server_cert_secret

    @server_cert_secret.setter
    def server_cert_secret(self, server_cert_secret):
        """Sets the server_cert_secret of this IoArgoprojEventsV1alpha1WebhookContext.

        ServerCertPath refers the file that contains the cert.  # noqa: E501

        :param server_cert_secret: The server_cert_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._server_cert_secret = server_cert_secret

    @property
    def server_key_secret(self):
        """Gets the server_key_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501


        :return: The server_key_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._server_key_secret

    @server_key_secret.setter
    def server_key_secret(self, server_key_secret):
        """Sets the server_key_secret of this IoArgoprojEventsV1alpha1WebhookContext.


        :param server_key_secret: The server_key_secret of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._server_key_secret = server_key_secret

    @property
    def url(self):
        """Gets the url of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501

        URL is the url of the server.  # noqa: E501

        :return: The url of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojEventsV1alpha1WebhookContext.

        URL is the url of the server.  # noqa: E501

        :param url: The url of this IoArgoprojEventsV1alpha1WebhookContext.  # noqa: E501
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
        if issubclass(IoArgoprojEventsV1alpha1WebhookContext, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1WebhookContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1WebhookContext):
            return True

        return self.to_dict() != other.to_dict()