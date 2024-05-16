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


class IoArgoprojWorkflowV1alpha1Parameter(object):
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
        'default': 'str',
        'description': 'str',
        'enum': 'list[str]',
        'global_name': 'str',
        'name': 'str',
        'value': 'str',
        'value_from': 'IoArgoprojWorkflowV1alpha1ValueFrom'
    }

    attribute_map = {
        'default': 'default',
        'description': 'description',
        'enum': 'enum',
        'global_name': 'globalName',
        'name': 'name',
        'value': 'value',
        'value_from': 'valueFrom'
    }

    def __init__(self, default=None, description=None, enum=None, global_name=None, name=None, value=None, value_from=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Parameter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default = None
        self._description = None
        self._enum = None
        self._global_name = None
        self._name = None
        self._value = None
        self._value_from = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if enum is not None:
            self.enum = enum
        if global_name is not None:
            self.global_name = global_name
        self.name = name
        if value is not None:
            self.value = value
        if value_from is not None:
            self.value_from = value_from

    @property
    def default(self):
        """Gets the default of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        Default is the default value to use for an input parameter if a value was not supplied  # noqa: E501

        :return: The default of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this IoArgoprojWorkflowV1alpha1Parameter.

        Default is the default value to use for an input parameter if a value was not supplied  # noqa: E501

        :param default: The default of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        Description is the parameter description  # noqa: E501

        :return: The description of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IoArgoprojWorkflowV1alpha1Parameter.

        Description is the parameter description  # noqa: E501

        :param description: The description of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enum(self):
        """Gets the enum of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        Enum holds a list of string values to choose from, for the actual value of the parameter  # noqa: E501

        :return: The enum of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this IoArgoprojWorkflowV1alpha1Parameter.

        Enum holds a list of string values to choose from, for the actual value of the parameter  # noqa: E501

        :param enum: The enum of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: list[str]
        """

        self._enum = enum

    @property
    def global_name(self):
        """Gets the global_name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        GlobalName exports an output parameter to the global scope, making it available as '{{io.argoproj.workflow.v1alpha1.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters  # noqa: E501

        :return: The global_name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._global_name

    @global_name.setter
    def global_name(self, global_name):
        """Sets the global_name of this IoArgoprojWorkflowV1alpha1Parameter.

        GlobalName exports an output parameter to the global scope, making it available as '{{io.argoproj.workflow.v1alpha1.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters  # noqa: E501

        :param global_name: The global_name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._global_name = global_name

    @property
    def name(self):
        """Gets the name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        Name is the parameter name  # noqa: E501

        :return: The name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojWorkflowV1alpha1Parameter.

        Name is the parameter name  # noqa: E501

        :param name: The name of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values  # noqa: E501

        :return: The value of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IoArgoprojWorkflowV1alpha1Parameter.

        Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values  # noqa: E501

        :param value: The value of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_from(self):
        """Gets the value_from of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501

        ValueFrom is the source for the output parameter's value  # noqa: E501

        :return: The value_from of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1ValueFrom
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this IoArgoprojWorkflowV1alpha1Parameter.

        ValueFrom is the source for the output parameter's value  # noqa: E501

        :param value_from: The value_from of this IoArgoprojWorkflowV1alpha1Parameter.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1ValueFrom
        """

        self._value_from = value_from

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
        if issubclass(IoArgoprojWorkflowV1alpha1Parameter, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Parameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1Parameter):
            return True

        return self.to_dict() != other.to_dict()