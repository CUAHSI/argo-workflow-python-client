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


class IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry(object):
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
        'api_version': 'str',
        'fields_type': 'str',
        'fields_v1': 'IoK8sApimachineryPkgApisMetaV1FieldsV1',
        'manager': 'str',
        'operation': 'str',
        'subresource': 'str',
        'time': 'IoK8sApimachineryPkgApisMetaV1Time'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'fields_type': 'fieldsType',
        'fields_v1': 'fieldsV1',
        'manager': 'manager',
        'operation': 'operation',
        'subresource': 'subresource',
        'time': 'time'
    }

    def __init__(self, api_version=None, fields_type=None, fields_v1=None, manager=None, operation=None, subresource=None, time=None, _configuration=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_version = None
        self._fields_type = None
        self._fields_v1 = None
        self._manager = None
        self._operation = None
        self._subresource = None
        self._time = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if fields_type is not None:
            self.fields_type = fields_type
        if fields_v1 is not None:
            self.fields_v1 = fields_v1
        if manager is not None:
            self.manager = manager
        if operation is not None:
            self.operation = operation
        if subresource is not None:
            self.subresource = subresource
        if time is not None:
            self.time = time

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        APIVersion defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.  # noqa: E501

        :return: The api_version of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        APIVersion defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.  # noqa: E501

        :param api_version: The api_version of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def fields_type(self):
        """Gets the fields_type of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \"FieldsV1\"  # noqa: E501

        :return: The fields_type of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._fields_type

    @fields_type.setter
    def fields_type(self, fields_type):
        """Sets the fields_type of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \"FieldsV1\"  # noqa: E501

        :param fields_type: The fields_type of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._fields_type = fields_type

    @property
    def fields_v1(self):
        """Gets the fields_v1 of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        FieldsV1 holds the first JSON version format as described in the \"FieldsV1\" type.  # noqa: E501

        :return: The fields_v1 of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1FieldsV1
        """
        return self._fields_v1

    @fields_v1.setter
    def fields_v1(self, fields_v1):
        """Sets the fields_v1 of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        FieldsV1 holds the first JSON version format as described in the \"FieldsV1\" type.  # noqa: E501

        :param fields_v1: The fields_v1 of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1FieldsV1
        """

        self._fields_v1 = fields_v1

    @property
    def manager(self):
        """Gets the manager of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        Manager is an identifier of the workflow managing these fields.  # noqa: E501

        :return: The manager of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        Manager is an identifier of the workflow managing these fields.  # noqa: E501

        :param manager: The manager of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def operation(self):
        """Gets the operation of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.  # noqa: E501

        :return: The operation of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.  # noqa: E501

        :param operation: The operation of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def subresource(self):
        """Gets the subresource of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.  # noqa: E501

        :return: The subresource of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._subresource

    @subresource.setter
    def subresource(self, subresource):
        """Sets the subresource of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.  # noqa: E501

        :param subresource: The subresource of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._subresource = subresource

    @property
    def time(self):
        """Gets the time of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501

        Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'  # noqa: E501

        :return: The time of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.

        Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'  # noqa: E501

        :param time: The time of this IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._time = time

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
        if issubclass(IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry):
            return True

        return self.to_dict() != other.to_dict()