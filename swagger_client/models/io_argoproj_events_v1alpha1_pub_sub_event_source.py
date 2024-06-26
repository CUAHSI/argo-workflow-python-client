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


class IoArgoprojEventsV1alpha1PubSubEventSource(object):
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
        'credential_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'delete_subscription_on_finish': 'bool',
        'filter': 'IoArgoprojEventsV1alpha1EventSourceFilter',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'project_id': 'str',
        'subscription_id': 'str',
        'topic': 'str',
        'topic_project_id': 'str'
    }

    attribute_map = {
        'credential_secret': 'credentialSecret',
        'delete_subscription_on_finish': 'deleteSubscriptionOnFinish',
        'filter': 'filter',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'project_id': 'projectID',
        'subscription_id': 'subscriptionID',
        'topic': 'topic',
        'topic_project_id': 'topicProjectID'
    }

    def __init__(self, credential_secret=None, delete_subscription_on_finish=None, filter=None, json_body=None, metadata=None, project_id=None, subscription_id=None, topic=None, topic_project_id=None, _configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1PubSubEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_secret = None
        self._delete_subscription_on_finish = None
        self._filter = None
        self._json_body = None
        self._metadata = None
        self._project_id = None
        self._subscription_id = None
        self._topic = None
        self._topic_project_id = None
        self.discriminator = None

        if credential_secret is not None:
            self.credential_secret = credential_secret
        if delete_subscription_on_finish is not None:
            self.delete_subscription_on_finish = delete_subscription_on_finish
        if filter is not None:
            self.filter = filter
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        if project_id is not None:
            self.project_id = project_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if topic is not None:
            self.topic = topic
        if topic_project_id is not None:
            self.topic_project_id = topic_project_id

    @property
    def credential_secret(self):
        """Gets the credential_secret of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The credential_secret of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._credential_secret

    @credential_secret.setter
    def credential_secret(self, credential_secret):
        """Sets the credential_secret of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param credential_secret: The credential_secret of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._credential_secret = credential_secret

    @property
    def delete_subscription_on_finish(self):
        """Gets the delete_subscription_on_finish of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The delete_subscription_on_finish of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._delete_subscription_on_finish

    @delete_subscription_on_finish.setter
    def delete_subscription_on_finish(self, delete_subscription_on_finish):
        """Sets the delete_subscription_on_finish of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param delete_subscription_on_finish: The delete_subscription_on_finish of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: bool
        """

        self._delete_subscription_on_finish = delete_subscription_on_finish

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1EventSourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param filter: The filter of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1EventSourceFilter
        """

        self._filter = filter

    @property
    def json_body(self):
        """Gets the json_body of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The json_body of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param json_body: The json_body of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def project_id(self):
        """Gets the project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param project_id: The project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The subscription_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param subscription_id: The subscription_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def topic(self):
        """Gets the topic of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The topic of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param topic: The topic of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def topic_project_id(self):
        """Gets the topic_project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501


        :return: The topic_project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic_project_id

    @topic_project_id.setter
    def topic_project_id(self, topic_project_id):
        """Sets the topic_project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.


        :param topic_project_id: The topic_project_id of this IoArgoprojEventsV1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._topic_project_id = topic_project_id

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
        if issubclass(IoArgoprojEventsV1alpha1PubSubEventSource, dict):
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
        if not isinstance(other, IoArgoprojEventsV1alpha1PubSubEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1PubSubEventSource):
            return True

        return self.to_dict() != other.to_dict()
