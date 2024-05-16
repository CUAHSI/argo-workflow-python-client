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


class EventsourceCreateEventSourceRequest(object):
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
        'event_source': 'IoArgoprojEventsV1alpha1EventSource',
        'namespace': 'str'
    }

    attribute_map = {
        'event_source': 'eventSource',
        'namespace': 'namespace'
    }

    def __init__(self, event_source=None, namespace=None, _configuration=None):  # noqa: E501
        """EventsourceCreateEventSourceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_source = None
        self._namespace = None
        self.discriminator = None

        if event_source is not None:
            self.event_source = event_source
        if namespace is not None:
            self.namespace = namespace

    @property
    def event_source(self):
        """Gets the event_source of this EventsourceCreateEventSourceRequest.  # noqa: E501


        :return: The event_source of this EventsourceCreateEventSourceRequest.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSource
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this EventsourceCreateEventSourceRequest.


        :param event_source: The event_source of this EventsourceCreateEventSourceRequest.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSource
        """

        self._event_source = event_source

    @property
    def namespace(self):
        """Gets the namespace of this EventsourceCreateEventSourceRequest.  # noqa: E501


        :return: The namespace of this EventsourceCreateEventSourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EventsourceCreateEventSourceRequest.


        :param namespace: The namespace of this EventsourceCreateEventSourceRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if issubclass(EventsourceCreateEventSourceRequest, dict):
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
        if not isinstance(other, EventsourceCreateEventSourceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventsourceCreateEventSourceRequest):
            return True

        return self.to_dict() != other.to_dict()