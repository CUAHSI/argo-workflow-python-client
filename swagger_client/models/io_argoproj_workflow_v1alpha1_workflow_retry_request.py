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


class IoArgoprojWorkflowV1alpha1WorkflowRetryRequest(object):
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
        'name': 'str',
        'namespace': 'str',
        'node_field_selector': 'str',
        'parameters': 'list[str]',
        'restart_successful': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'node_field_selector': 'nodeFieldSelector',
        'parameters': 'parameters',
        'restart_successful': 'restartSuccessful'
    }

    def __init__(self, name=None, namespace=None, node_field_selector=None, parameters=None, restart_successful=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowRetryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._namespace = None
        self._node_field_selector = None
        self._parameters = None
        self._restart_successful = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if node_field_selector is not None:
            self.node_field_selector = node_field_selector
        if parameters is not None:
            self.parameters = parameters
        if restart_successful is not None:
            self.restart_successful = restart_successful

    @property
    def name(self):
        """Gets the name of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501


        :return: The name of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.


        :param name: The name of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501


        :return: The namespace of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.


        :param namespace: The namespace of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def node_field_selector(self):
        """Gets the node_field_selector of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501


        :return: The node_field_selector of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_field_selector

    @node_field_selector.setter
    def node_field_selector(self, node_field_selector):
        """Sets the node_field_selector of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.


        :param node_field_selector: The node_field_selector of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :type: str
        """

        self._node_field_selector = node_field_selector

    @property
    def parameters(self):
        """Gets the parameters of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501


        :return: The parameters of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.


        :param parameters: The parameters of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :type: list[str]
        """

        self._parameters = parameters

    @property
    def restart_successful(self):
        """Gets the restart_successful of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501


        :return: The restart_successful of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._restart_successful

    @restart_successful.setter
    def restart_successful(self, restart_successful):
        """Sets the restart_successful of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.


        :param restart_successful: The restart_successful of this IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.  # noqa: E501
        :type: bool
        """

        self._restart_successful = restart_successful

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
        if issubclass(IoArgoprojWorkflowV1alpha1WorkflowRetryRequest, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowRetryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowRetryRequest):
            return True

        return self.to_dict() != other.to_dict()
