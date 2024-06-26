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


class IoArgoprojEventsV1alpha1WebhookEventSource(object):
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
        'webhook_context': 'IoArgoprojEventsV1alpha1WebhookContext'
    }

    attribute_map = {
        'filter': 'filter',
        'webhook_context': 'webhookContext'
    }

    def __init__(self, filter=None, webhook_context=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1WebhookEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter = None
        self._webhook_context = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if webhook_context is not None:
            self.webhook_context = webhook_context

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1WebhookEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def webhook_context(self):
        """Gets the webhook_context of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501


        :return: The webhook_context of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WebhookContext
        """
        return self._webhook_context

    @webhook_context.setter
    def webhook_context(self, webhook_context):
        """Sets the webhook_context of this IoArgoprojEventsV1alpha1WebhookEventSource.


        :param webhook_context: The webhook_context of this IoArgoprojEventsV1alpha1WebhookEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1WebhookContext
        """

        self._webhook_context = webhook_context

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
        if issubclass(IoArgoprojEventsV1alpha1WebhookEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1WebhookEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1WebhookEventSource):
            return True

        return self.to_dict() != other.to_dict()
