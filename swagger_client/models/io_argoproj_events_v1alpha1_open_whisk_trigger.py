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


class IoArgoprojEventsV1alpha1OpenWhiskTrigger(object):
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
        'action_name': 'str',
        'auth_token': 'IoK8sApiCoreV1SecretKeySelector',
        'host': 'str',
        'namespace': 'str',
        'parameters': 'list[IoArgoprojEventsV1alpha1TriggerParameter]',
        'payload': 'list[IoArgoprojEventsV1alpha1TriggerParameter]',
        'version': 'str'
    }

    attribute_map = {
        'action_name': 'actionName',
        'auth_token': 'authToken',
        'host': 'host',
        'namespace': 'namespace',
        'parameters': 'parameters',
        'payload': 'payload',
        'version': 'version'
    }

    def __init__(self, action_name=None, auth_token=None, host=None, namespace=None, parameters=None, payload=None, version=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1OpenWhiskTrigger - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_name = None
        self._auth_token = None
        self._host = None
        self._namespace = None
        self._parameters = None
        self._payload = None
        self._version = None
        self.discriminator = None

        if action_name is not None:
            self.action_name = action_name
        if auth_token is not None:
            self.auth_token = auth_token
        if host is not None:
            self.host = host
        if namespace is not None:
            self.namespace = namespace
        if parameters is not None:
            self.parameters = parameters
        if payload is not None:
            self.payload = payload
        if version is not None:
            self.version = version

    @property
    def action_name(self):
        """Gets the action_name of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501

        Name of the action/function.  # noqa: E501

        :return: The action_name of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.

        Name of the action/function.  # noqa: E501

        :param action_name: The action_name of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def auth_token(self):
        """Gets the auth_token of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The auth_token of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.


        :param auth_token: The auth_token of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._auth_token = auth_token

    @property
    def host(self):
        """Gets the host of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501

        Host URL of the OpenWhisk.  # noqa: E501

        :return: The host of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.

        Host URL of the OpenWhisk.  # noqa: E501

        :param host: The host of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def namespace(self):
        """Gets the namespace of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501

        Namespace for the action. Defaults to \"_\". +optional.  # noqa: E501

        :return: The namespace of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.

        Namespace for the action. Defaults to \"_\". +optional.  # noqa: E501

        :param namespace: The namespace of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def parameters(self):
        """Gets the parameters of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The parameters of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.


        :param parameters: The parameters of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """

        self._parameters = parameters

    @property
    def payload(self):
        """Gets the payload of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501

        Payload is the list of key-value extracted from an event payload to construct the request payload.  # noqa: E501

        :return: The payload of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.

        Payload is the list of key-value extracted from an event payload to construct the request payload.  # noqa: E501

        :param payload: The payload of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1TriggerParameter]
        """

        self._payload = payload

    @property
    def version(self):
        """Gets the version of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The version of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.


        :param version: The version of this IoArgoprojEventsV1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(IoArgoprojEventsV1alpha1OpenWhiskTrigger, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1OpenWhiskTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1OpenWhiskTrigger):
            return True

        return self.to_dict() != other.to_dict()