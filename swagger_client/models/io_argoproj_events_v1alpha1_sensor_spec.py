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


class IoArgoprojEventsV1alpha1SensorSpec(object):
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
        'dependencies': 'list[IoArgoprojEventsV1alpha1EventDependency]',
        'error_on_failed_round': 'bool',
        'event_bus_name': 'str',
        'replicas': 'int',
        'template': 'IoArgoprojEventsV1alpha1Template',
        'triggers': 'list[IoArgoprojEventsV1alpha1Trigger]'
    }

    attribute_map = {
        'dependencies': 'dependencies',
        'error_on_failed_round': 'errorOnFailedRound',
        'event_bus_name': 'eventBusName',
        'replicas': 'replicas',
        'template': 'template',
        'triggers': 'triggers'
    }

    def __init__(self, dependencies=None, error_on_failed_round=None, event_bus_name=None, replicas=None, template=None, triggers=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1SensorSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dependencies = None
        self._error_on_failed_round = None
        self._event_bus_name = None
        self._replicas = None
        self._template = None
        self._triggers = None
        self.discriminator = None

        if dependencies is not None:
            self.dependencies = dependencies
        if error_on_failed_round is not None:
            self.error_on_failed_round = error_on_failed_round
        if event_bus_name is not None:
            self.event_bus_name = event_bus_name
        if replicas is not None:
            self.replicas = replicas
        if template is not None:
            self.template = template
        if triggers is not None:
            self.triggers = triggers

    @property
    def dependencies(self):
        """Gets the dependencies of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501

        Dependencies is a list of the events that this sensor is dependent on.  # noqa: E501

        :return: The dependencies of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1EventDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this IoArgoprojEventsV1alpha1SensorSpec.

        Dependencies is a list of the events that this sensor is dependent on.  # noqa: E501

        :param dependencies: The dependencies of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1EventDependency]
        """

        self._dependencies = dependencies

    @property
    def error_on_failed_round(self):
        """Gets the error_on_failed_round of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501

        ErrorOnFailedRound if set to true, marks sensor state as `error` if the previous trigger round fails. Once sensor state is set to `error`, no further triggers will be processed.  # noqa: E501

        :return: The error_on_failed_round of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: bool
        """
        return self._error_on_failed_round

    @error_on_failed_round.setter
    def error_on_failed_round(self, error_on_failed_round):
        """Sets the error_on_failed_round of this IoArgoprojEventsV1alpha1SensorSpec.

        ErrorOnFailedRound if set to true, marks sensor state as `error` if the previous trigger round fails. Once sensor state is set to `error`, no further triggers will be processed.  # noqa: E501

        :param error_on_failed_round: The error_on_failed_round of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: bool
        """

        self._error_on_failed_round = error_on_failed_round

    @property
    def event_bus_name(self):
        """Gets the event_bus_name of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501


        :return: The event_bus_name of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: str
        """
        return self._event_bus_name

    @event_bus_name.setter
    def event_bus_name(self, event_bus_name):
        """Sets the event_bus_name of this IoArgoprojEventsV1alpha1SensorSpec.


        :param event_bus_name: The event_bus_name of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: str
        """

        self._event_bus_name = event_bus_name

    @property
    def replicas(self):
        """Gets the replicas of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501


        :return: The replicas of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this IoArgoprojEventsV1alpha1SensorSpec.


        :param replicas: The replicas of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def template(self):
        """Gets the template of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501


        :return: The template of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this IoArgoprojEventsV1alpha1SensorSpec.


        :param template: The template of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Template
        """

        self._template = template

    @property
    def triggers(self):
        """Gets the triggers of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501

        Triggers is a list of the things that this sensor evokes. These are the outputs from this sensor.  # noqa: E501

        :return: The triggers of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this IoArgoprojEventsV1alpha1SensorSpec.

        Triggers is a list of the things that this sensor evokes. These are the outputs from this sensor.  # noqa: E501

        :param triggers: The triggers of this IoArgoprojEventsV1alpha1SensorSpec.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1Trigger]
        """

        self._triggers = triggers

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
        if issubclass(IoArgoprojEventsV1alpha1SensorSpec, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1SensorSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1SensorSpec):
            return True

        return self.to_dict() != other.to_dict()
