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


class IoArgoprojEventsV1alpha1BitbucketServerEventSource(object):
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
        'bitbucketserver_base_url': 'str',
        'delete_hook_on_finish': 'bool',
        'events': 'list[str]',
        'filter': 'IoArgoprojEventsV1alpha1EventSourceFilter',
        'metadata': 'dict(str, str)',
        'project_key': 'str',
        'repositories': 'list[IoArgoprojEventsV1alpha1BitbucketServerRepository]',
        'repository_slug': 'str',
        'webhook': 'IoArgoprojEventsV1alpha1WebhookContext',
        'webhook_secret': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'bitbucketserver_base_url': 'bitbucketserverBaseURL',
        'delete_hook_on_finish': 'deleteHookOnFinish',
        'events': 'events',
        'filter': 'filter',
        'metadata': 'metadata',
        'project_key': 'projectKey',
        'repositories': 'repositories',
        'repository_slug': 'repositorySlug',
        'webhook': 'webhook',
        'webhook_secret': 'webhookSecret'
    }

    def __init__(self, access_token=None, bitbucketserver_base_url=None, delete_hook_on_finish=None, events=None, filter=None, metadata=None, project_key=None, repositories=None, repository_slug=None, webhook=None, webhook_secret=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1BitbucketServerEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._bitbucketserver_base_url = None
        self._delete_hook_on_finish = None
        self._events = None
        self._filter = None
        self._metadata = None
        self._project_key = None
        self._repositories = None
        self._repository_slug = None
        self._webhook = None
        self._webhook_secret = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if bitbucketserver_base_url is not None:
            self.bitbucketserver_base_url = bitbucketserver_base_url
        if delete_hook_on_finish is not None:
            self.delete_hook_on_finish = delete_hook_on_finish
        if events is not None:
            self.events = events
        if filter is not None:
            self.filter = filter
        if metadata is not None:
            self.metadata = metadata
        if project_key is not None:
            self.project_key = project_key
        if repositories is not None:
            self.repositories = repositories
        if repository_slug is not None:
            self.repository_slug = repository_slug
        if webhook is not None:
            self.webhook = webhook
        if webhook_secret is not None:
            self.webhook_secret = webhook_secret

    @property
    def access_token(self):
        """Gets the access_token of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The access_token of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param access_token: The access_token of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._access_token = access_token

    @property
    def bitbucketserver_base_url(self):
        """Gets the bitbucketserver_base_url of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The bitbucketserver_base_url of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: str
        """
        return self._bitbucketserver_base_url

    @bitbucketserver_base_url.setter
    def bitbucketserver_base_url(self, bitbucketserver_base_url):
        """Sets the bitbucketserver_base_url of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param bitbucketserver_base_url: The bitbucketserver_base_url of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: str
        """

        self._bitbucketserver_base_url = bitbucketserver_base_url

    @property
    def delete_hook_on_finish(self):
        """Gets the delete_hook_on_finish of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The delete_hook_on_finish of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._delete_hook_on_finish

    @delete_hook_on_finish.setter
    def delete_hook_on_finish(self, delete_hook_on_finish):
        """Sets the delete_hook_on_finish of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param delete_hook_on_finish: The delete_hook_on_finish of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: bool
        """

        self._delete_hook_on_finish = delete_hook_on_finish

    @property
    def events(self):
        """Gets the events of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The events of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param events: The events of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def project_key(self):
        """Gets the project_key of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The project_key of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: str
        """
        return self._project_key

    @project_key.setter
    def project_key(self, project_key):
        """Sets the project_key of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param project_key: The project_key of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: str
        """

        self._project_key = project_key

    @property
    def repositories(self):
        """Gets the repositories of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The repositories of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: list[IoArgoprojEventsV1alpha1BitbucketServerRepository]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param repositories: The repositories of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: list[IoArgoprojEventsV1alpha1BitbucketServerRepository]
        """

        self._repositories = repositories

    @property
    def repository_slug(self):
        """Gets the repository_slug of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The repository_slug of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: str
        """
        return self._repository_slug

    @repository_slug.setter
    def repository_slug(self, repository_slug):
        """Sets the repository_slug of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param repository_slug: The repository_slug of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: str
        """

        self._repository_slug = repository_slug

    @property
    def webhook(self):
        """Gets the webhook of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The webhook of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WebhookContext
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param webhook: The webhook of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1WebhookContext
        """

        self._webhook = webhook

    @property
    def webhook_secret(self):
        """Gets the webhook_secret of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501


        :return: The webhook_secret of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._webhook_secret

    @webhook_secret.setter
    def webhook_secret(self, webhook_secret):
        """Sets the webhook_secret of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.


        :param webhook_secret: The webhook_secret of this IoArgoprojEventsV1alpha1BitbucketServerEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._webhook_secret = webhook_secret

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
        if issubclass(IoArgoprojEventsV1alpha1BitbucketServerEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1BitbucketServerEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1BitbucketServerEventSource):
            return True

        return self.to_dict() != other.to_dict()
