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


class IoArgoprojWorkflowV1alpha1GCSArtifact(object):
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
        'bucket': 'str',
        'key': 'str',
        'service_account_key_secret': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'bucket': 'bucket',
        'key': 'key',
        'service_account_key_secret': 'serviceAccountKeySecret'
    }

    def __init__(self, bucket=None, key=None, service_account_key_secret=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1GCSArtifact - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket = None
        self._key = None
        self._service_account_key_secret = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        self.key = key
        if service_account_key_secret is not None:
            self.service_account_key_secret = service_account_key_secret

    @property
    def bucket(self):
        """Gets the bucket of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501

        Bucket is the name of the bucket  # noqa: E501

        :return: The bucket of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this IoArgoprojWorkflowV1alpha1GCSArtifact.

        Bucket is the name of the bucket  # noqa: E501

        :param bucket: The bucket of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def key(self):
        """Gets the key of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501

        Key is the path in the bucket where the artifact resides  # noqa: E501

        :return: The key of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoArgoprojWorkflowV1alpha1GCSArtifact.

        Key is the path in the bucket where the artifact resides  # noqa: E501

        :param key: The key of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def service_account_key_secret(self):
        """Gets the service_account_key_secret of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501

        ServiceAccountKeySecret is the secret selector to the bucket's service account key  # noqa: E501

        :return: The service_account_key_secret of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._service_account_key_secret

    @service_account_key_secret.setter
    def service_account_key_secret(self, service_account_key_secret):
        """Sets the service_account_key_secret of this IoArgoprojWorkflowV1alpha1GCSArtifact.

        ServiceAccountKeySecret is the secret selector to the bucket's service account key  # noqa: E501

        :param service_account_key_secret: The service_account_key_secret of this IoArgoprojWorkflowV1alpha1GCSArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._service_account_key_secret = service_account_key_secret

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
        if issubclass(IoArgoprojWorkflowV1alpha1GCSArtifact, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1GCSArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1GCSArtifact):
            return True

        return self.to_dict() != other.to_dict()
