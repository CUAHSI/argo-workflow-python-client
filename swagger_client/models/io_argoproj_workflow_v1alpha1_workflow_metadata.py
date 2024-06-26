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


class IoArgoprojWorkflowV1alpha1WorkflowMetadata(object):
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
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)',
        'labels_from': 'dict(str, IoArgoprojWorkflowV1alpha1LabelValueFrom)'
    }

    attribute_map = {
        'annotations': 'annotations',
        'labels': 'labels',
        'labels_from': 'labelsFrom'
    }

    def __init__(self, annotations=None, labels=None, labels_from=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotations = None
        self._labels = None
        self._labels_from = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels
        if labels_from is not None:
            self.labels_from = labels_from

    @property
    def annotations(self):
        """Gets the annotations of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501


        :return: The annotations of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.


        :param annotations: The annotations of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501


        :return: The labels of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.


        :param labels: The labels of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def labels_from(self):
        """Gets the labels_from of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501


        :return: The labels_from of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :rtype: dict(str, IoArgoprojWorkflowV1alpha1LabelValueFrom)
        """
        return self._labels_from

    @labels_from.setter
    def labels_from(self, labels_from):
        """Sets the labels_from of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.


        :param labels_from: The labels_from of this IoArgoprojWorkflowV1alpha1WorkflowMetadata.  # noqa: E501
        :type: dict(str, IoArgoprojWorkflowV1alpha1LabelValueFrom)
        """

        self._labels_from = labels_from

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
        if issubclass(IoArgoprojWorkflowV1alpha1WorkflowMetadata, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowMetadata):
            return True

        return self.to_dict() != other.to_dict()
