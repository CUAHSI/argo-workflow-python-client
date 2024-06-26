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


class IoArgoprojEventsV1alpha1GitlabEventSource(object):
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
        'access_token': 'IoK8sApiCoreV1SecretKeySelector',
        'delete_hook_on_finish': 'bool',
        'enable_ssl_verification': 'bool',
        'events': 'list[str]',
        'filter': 'IoArgoprojEventsV1alpha1EventSourceFilter',
        'gitlab_base_url': 'str',
        'metadata': 'dict(str, str)',
        'project_id': 'str',
        'projects': 'list[str]',
        'secret_token': 'IoK8sApiCoreV1SecretKeySelector',
        'webhook': 'IoArgoprojEventsV1alpha1WebhookContext'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'delete_hook_on_finish': 'deleteHookOnFinish',
        'enable_ssl_verification': 'enableSSLVerification',
        'events': 'events',
        'filter': 'filter',
        'gitlab_base_url': 'gitlabBaseURL',
        'metadata': 'metadata',
        'project_id': 'projectID',
        'projects': 'projects',
        'secret_token': 'secretToken',
        'webhook': 'webhook'
    }

    def __init__(self, access_token=None, delete_hook_on_finish=None, enable_ssl_verification=None, events=None, filter=None, gitlab_base_url=None, metadata=None, project_id=None, projects=None, secret_token=None, webhook=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1GitlabEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._delete_hook_on_finish = None
        self._enable_ssl_verification = None
        self._events = None
        self._filter = None
        self._gitlab_base_url = None
        self._metadata = None
        self._project_id = None
        self._projects = None
        self._secret_token = None
        self._webhook = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if delete_hook_on_finish is not None:
            self.delete_hook_on_finish = delete_hook_on_finish
        if enable_ssl_verification is not None:
            self.enable_ssl_verification = enable_ssl_verification
        if events is not None:
            self.events = events
        if filter is not None:
            self.filter = filter
        if gitlab_base_url is not None:
            self.gitlab_base_url = gitlab_base_url
        if metadata is not None:
            self.metadata = metadata
        if project_id is not None:
            self.project_id = project_id
        if projects is not None:
            self.projects = projects
        if secret_token is not None:
            self.secret_token = secret_token
        if webhook is not None:
            self.webhook = webhook

    @property
    def access_token(self):
        """Gets the access_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The access_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param access_token: The access_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._access_token = access_token

    @property
    def delete_hook_on_finish(self):
        """Gets the delete_hook_on_finish of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The delete_hook_on_finish of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._delete_hook_on_finish

    @delete_hook_on_finish.setter
    def delete_hook_on_finish(self, delete_hook_on_finish):
        """Sets the delete_hook_on_finish of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param delete_hook_on_finish: The delete_hook_on_finish of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: bool
        """

        self._delete_hook_on_finish = delete_hook_on_finish

    @property
    def enable_ssl_verification(self):
        """Gets the enable_ssl_verification of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The enable_ssl_verification of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssl_verification

    @enable_ssl_verification.setter
    def enable_ssl_verification(self, enable_ssl_verification):
        """Sets the enable_ssl_verification of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param enable_ssl_verification: The enable_ssl_verification of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: bool
        """

        self._enable_ssl_verification = enable_ssl_verification

    @property
    def events(self):
        """Gets the events of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501

        Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794.  # noqa: E501

        :return: The events of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this IoArgoprojEventsV1alpha1GitlabEventSource.

        Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794.  # noqa: E501

        :param events: The events of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def gitlab_base_url(self):
        """Gets the gitlab_base_url of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The gitlab_base_url of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: str
        """
        return self._gitlab_base_url

    @gitlab_base_url.setter
    def gitlab_base_url(self, gitlab_base_url):
        """Sets the gitlab_base_url of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param gitlab_base_url: The gitlab_base_url of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: str
        """

        self._gitlab_base_url = gitlab_base_url

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def project_id(self):
        """Gets the project_id of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The project_id of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param project_id: The project_id of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def projects(self):
        """Gets the projects of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The projects of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param projects: The projects of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: list[str]
        """

        self._projects = projects

    @property
    def secret_token(self):
        """Gets the secret_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The secret_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._secret_token

    @secret_token.setter
    def secret_token(self, secret_token):
        """Sets the secret_token of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param secret_token: The secret_token of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._secret_token = secret_token

    @property
    def webhook(self):
        """Gets the webhook of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501


        :return: The webhook of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WebhookContext
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this IoArgoprojEventsV1alpha1GitlabEventSource.


        :param webhook: The webhook of this IoArgoprojEventsV1alpha1GitlabEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1WebhookContext
        """

        self._webhook = webhook

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
        if issubclass(IoArgoprojEventsV1alpha1GitlabEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1GitlabEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1GitlabEventSource):
            return True

        return self.to_dict() != other.to_dict()
