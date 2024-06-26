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


class IoArgoprojWorkflowV1alpha1AzureArtifactRepository(object):
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
        'account_key_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'blob_name_format': 'str',
        'container': 'str',
        'endpoint': 'str',
        'use_sdk_creds': 'bool'
    }

    attribute_map = {
        'account_key_secret': 'accountKeySecret',
        'blob_name_format': 'blobNameFormat',
        'container': 'container',
        'endpoint': 'endpoint',
        'use_sdk_creds': 'useSDKCreds'
    }

    def __init__(self, account_key_secret=None, blob_name_format=None, container=None, endpoint=None, use_sdk_creds=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1AzureArtifactRepository - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_key_secret = None
        self._blob_name_format = None
        self._container = None
        self._endpoint = None
        self._use_sdk_creds = None
        self.discriminator = None

        if account_key_secret is not None:
            self.account_key_secret = account_key_secret
        if blob_name_format is not None:
            self.blob_name_format = blob_name_format
        self.container = container
        self.endpoint = endpoint
        if use_sdk_creds is not None:
            self.use_sdk_creds = use_sdk_creds

    @property
    def account_key_secret(self):
        """Gets the account_key_secret of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501

        AccountKeySecret is the secret selector to the Azure Blob Storage account access key  # noqa: E501

        :return: The account_key_secret of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._account_key_secret

    @account_key_secret.setter
    def account_key_secret(self, account_key_secret):
        """Sets the account_key_secret of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.

        AccountKeySecret is the secret selector to the Azure Blob Storage account access key  # noqa: E501

        :param account_key_secret: The account_key_secret of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._account_key_secret = account_key_secret

    @property
    def blob_name_format(self):
        """Gets the blob_name_format of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501

        BlobNameFormat is defines the format of how to store blob names. Can reference workflow variables  # noqa: E501

        :return: The blob_name_format of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :rtype: str
        """
        return self._blob_name_format

    @blob_name_format.setter
    def blob_name_format(self, blob_name_format):
        """Sets the blob_name_format of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.

        BlobNameFormat is defines the format of how to store blob names. Can reference workflow variables  # noqa: E501

        :param blob_name_format: The blob_name_format of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :type: str
        """

        self._blob_name_format = blob_name_format

    @property
    def container(self):
        """Gets the container of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501

        Container is the container where resources will be stored  # noqa: E501

        :return: The container of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.

        Container is the container where resources will be stored  # noqa: E501

        :param container: The container of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and container is None:
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501

        self._container = container

    @property
    def endpoint(self):
        """Gets the endpoint of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501

        Endpoint is the service url associated with an account. It is most likely \"https://<ACCOUNT_NAME>.blob.core.windows.net\"  # noqa: E501

        :return: The endpoint of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.

        Endpoint is the service url associated with an account. It is most likely \"https://<ACCOUNT_NAME>.blob.core.windows.net\"  # noqa: E501

        :param endpoint: The endpoint of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def use_sdk_creds(self):
        """Gets the use_sdk_creds of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501

        UseSDKCreds tells the driver to figure out credentials based on sdk defaults.  # noqa: E501

        :return: The use_sdk_creds of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :rtype: bool
        """
        return self._use_sdk_creds

    @use_sdk_creds.setter
    def use_sdk_creds(self, use_sdk_creds):
        """Sets the use_sdk_creds of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.

        UseSDKCreds tells the driver to figure out credentials based on sdk defaults.  # noqa: E501

        :param use_sdk_creds: The use_sdk_creds of this IoArgoprojWorkflowV1alpha1AzureArtifactRepository.  # noqa: E501
        :type: bool
        """

        self._use_sdk_creds = use_sdk_creds

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
        if issubclass(IoArgoprojWorkflowV1alpha1AzureArtifactRepository, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1AzureArtifactRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1AzureArtifactRepository):
            return True

        return self.to_dict() != other.to_dict()
