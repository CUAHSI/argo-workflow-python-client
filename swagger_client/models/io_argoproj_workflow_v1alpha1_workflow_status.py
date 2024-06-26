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


class IoArgoprojWorkflowV1alpha1WorkflowStatus(object):
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
        'artifact_gc_status': 'IoArgoprojWorkflowV1alpha1ArtGCStatus',
        'artifact_repository_ref': 'IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus',
        'compressed_nodes': 'str',
        'conditions': 'list[IoArgoprojWorkflowV1alpha1Condition]',
        'estimated_duration': 'int',
        'finished_at': 'IoK8sApimachineryPkgApisMetaV1Time',
        'message': 'str',
        'nodes': 'dict(str, IoArgoprojWorkflowV1alpha1NodeStatus)',
        'offload_node_status_version': 'str',
        'outputs': 'IoArgoprojWorkflowV1alpha1Outputs',
        'persistent_volume_claims': 'list[IoK8sApiCoreV1Volume]',
        'phase': 'str',
        'progress': 'str',
        'resources_duration': 'dict(str, int)',
        'started_at': 'IoK8sApimachineryPkgApisMetaV1Time',
        'stored_templates': 'dict(str, IoArgoprojWorkflowV1alpha1Template)',
        'stored_workflow_template_spec': 'IoArgoprojWorkflowV1alpha1WorkflowSpec',
        'synchronization': 'IoArgoprojWorkflowV1alpha1SynchronizationStatus',
        'task_results_completion_status': 'dict(str, bool)'
    }

    attribute_map = {
        'artifact_gc_status': 'artifactGCStatus',
        'artifact_repository_ref': 'artifactRepositoryRef',
        'compressed_nodes': 'compressedNodes',
        'conditions': 'conditions',
        'estimated_duration': 'estimatedDuration',
        'finished_at': 'finishedAt',
        'message': 'message',
        'nodes': 'nodes',
        'offload_node_status_version': 'offloadNodeStatusVersion',
        'outputs': 'outputs',
        'persistent_volume_claims': 'persistentVolumeClaims',
        'phase': 'phase',
        'progress': 'progress',
        'resources_duration': 'resourcesDuration',
        'started_at': 'startedAt',
        'stored_templates': 'storedTemplates',
        'stored_workflow_template_spec': 'storedWorkflowTemplateSpec',
        'synchronization': 'synchronization',
        'task_results_completion_status': 'taskResultsCompletionStatus'
    }

    def __init__(self, artifact_gc_status=None, artifact_repository_ref=None, compressed_nodes=None, conditions=None, estimated_duration=None, finished_at=None, message=None, nodes=None, offload_node_status_version=None, outputs=None, persistent_volume_claims=None, phase=None, progress=None, resources_duration=None, started_at=None, stored_templates=None, stored_workflow_template_spec=None, synchronization=None, task_results_completion_status=None, _configuration=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artifact_gc_status = None
        self._artifact_repository_ref = None
        self._compressed_nodes = None
        self._conditions = None
        self._estimated_duration = None
        self._finished_at = None
        self._message = None
        self._nodes = None
        self._offload_node_status_version = None
        self._outputs = None
        self._persistent_volume_claims = None
        self._phase = None
        self._progress = None
        self._resources_duration = None
        self._started_at = None
        self._stored_templates = None
        self._stored_workflow_template_spec = None
        self._synchronization = None
        self._task_results_completion_status = None
        self.discriminator = None

        if artifact_gc_status is not None:
            self.artifact_gc_status = artifact_gc_status
        if artifact_repository_ref is not None:
            self.artifact_repository_ref = artifact_repository_ref
        if compressed_nodes is not None:
            self.compressed_nodes = compressed_nodes
        if conditions is not None:
            self.conditions = conditions
        if estimated_duration is not None:
            self.estimated_duration = estimated_duration
        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        if nodes is not None:
            self.nodes = nodes
        if offload_node_status_version is not None:
            self.offload_node_status_version = offload_node_status_version
        if outputs is not None:
            self.outputs = outputs
        if persistent_volume_claims is not None:
            self.persistent_volume_claims = persistent_volume_claims
        if phase is not None:
            self.phase = phase
        if progress is not None:
            self.progress = progress
        if resources_duration is not None:
            self.resources_duration = resources_duration
        if started_at is not None:
            self.started_at = started_at
        if stored_templates is not None:
            self.stored_templates = stored_templates
        if stored_workflow_template_spec is not None:
            self.stored_workflow_template_spec = stored_workflow_template_spec
        if synchronization is not None:
            self.synchronization = synchronization
        if task_results_completion_status is not None:
            self.task_results_completion_status = task_results_completion_status

    @property
    def artifact_gc_status(self):
        """Gets the artifact_gc_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        ArtifactGCStatus maintains the status of Artifact Garbage Collection  # noqa: E501

        :return: The artifact_gc_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1ArtGCStatus
        """
        return self._artifact_gc_status

    @artifact_gc_status.setter
    def artifact_gc_status(self, artifact_gc_status):
        """Sets the artifact_gc_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        ArtifactGCStatus maintains the status of Artifact Garbage Collection  # noqa: E501

        :param artifact_gc_status: The artifact_gc_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1ArtGCStatus
        """

        self._artifact_gc_status = artifact_gc_status

    @property
    def artifact_repository_ref(self):
        """Gets the artifact_repository_ref of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        ArtifactRepositoryRef is used to cache the repository to use so we do not need to determine it everytime we reconcile.  # noqa: E501

        :return: The artifact_repository_ref of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus
        """
        return self._artifact_repository_ref

    @artifact_repository_ref.setter
    def artifact_repository_ref(self, artifact_repository_ref):
        """Sets the artifact_repository_ref of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        ArtifactRepositoryRef is used to cache the repository to use so we do not need to determine it everytime we reconcile.  # noqa: E501

        :param artifact_repository_ref: The artifact_repository_ref of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus
        """

        self._artifact_repository_ref = artifact_repository_ref

    @property
    def compressed_nodes(self):
        """Gets the compressed_nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Compressed and base64 decoded Nodes map  # noqa: E501

        :return: The compressed_nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._compressed_nodes

    @compressed_nodes.setter
    def compressed_nodes(self, compressed_nodes):
        """Sets the compressed_nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Compressed and base64 decoded Nodes map  # noqa: E501

        :param compressed_nodes: The compressed_nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._compressed_nodes = compressed_nodes

    @property
    def conditions(self):
        """Gets the conditions of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Conditions is a list of conditions the Workflow may have  # noqa: E501

        :return: The conditions of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: list[IoArgoprojWorkflowV1alpha1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Conditions is a list of conditions the Workflow may have  # noqa: E501

        :param conditions: The conditions of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: list[IoArgoprojWorkflowV1alpha1Condition]
        """

        self._conditions = conditions

    @property
    def estimated_duration(self):
        """Gets the estimated_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        EstimatedDuration in seconds.  # noqa: E501

        :return: The estimated_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: int
        """
        return self._estimated_duration

    @estimated_duration.setter
    def estimated_duration(self, estimated_duration):
        """Sets the estimated_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        EstimatedDuration in seconds.  # noqa: E501

        :param estimated_duration: The estimated_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: int
        """

        self._estimated_duration = estimated_duration

    @property
    def finished_at(self):
        """Gets the finished_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Time at which this workflow completed  # noqa: E501

        :return: The finished_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Time at which this workflow completed  # noqa: E501

        :param finished_at: The finished_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        A human readable message indicating details about why the workflow is in this condition.  # noqa: E501

        :return: The message of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        A human readable message indicating details about why the workflow is in this condition.  # noqa: E501

        :param message: The message of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def nodes(self):
        """Gets the nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Nodes is a mapping between a node ID and the node's status.  # noqa: E501

        :return: The nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, IoArgoprojWorkflowV1alpha1NodeStatus)
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Nodes is a mapping between a node ID and the node's status.  # noqa: E501

        :param nodes: The nodes of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, IoArgoprojWorkflowV1alpha1NodeStatus)
        """

        self._nodes = nodes

    @property
    def offload_node_status_version(self):
        """Gets the offload_node_status_version of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.  # noqa: E501

        :return: The offload_node_status_version of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._offload_node_status_version

    @offload_node_status_version.setter
    def offload_node_status_version(self, offload_node_status_version):
        """Sets the offload_node_status_version of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.  # noqa: E501

        :param offload_node_status_version: The offload_node_status_version of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._offload_node_status_version = offload_node_status_version

    @property
    def outputs(self):
        """Gets the outputs of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Outputs captures output values and artifact locations produced by the workflow via global outputs  # noqa: E501

        :return: The outputs of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1Outputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Outputs captures output values and artifact locations produced by the workflow via global outputs  # noqa: E501

        :param outputs: The outputs of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1Outputs
        """

        self._outputs = outputs

    @property
    def persistent_volume_claims(self):
        """Gets the persistent_volume_claims of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        PersistentVolumeClaims tracks all PVCs that were created as part of the io.argoproj.workflow.v1alpha1. The contents of this list are drained at the end of the workflow.  # noqa: E501

        :return: The persistent_volume_claims of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1Volume]
        """
        return self._persistent_volume_claims

    @persistent_volume_claims.setter
    def persistent_volume_claims(self, persistent_volume_claims):
        """Sets the persistent_volume_claims of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        PersistentVolumeClaims tracks all PVCs that were created as part of the io.argoproj.workflow.v1alpha1. The contents of this list are drained at the end of the workflow.  # noqa: E501

        :param persistent_volume_claims: The persistent_volume_claims of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: list[IoK8sApiCoreV1Volume]
        """

        self._persistent_volume_claims = persistent_volume_claims

    @property
    def phase(self):
        """Gets the phase of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Phase a simple, high-level summary of where the workflow is in its lifecycle. Will be \"\" (Unknown), \"Pending\", or \"Running\" before the workflow is completed, and \"Succeeded\", \"Failed\" or \"Error\" once the workflow has completed.  # noqa: E501

        :return: The phase of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Phase a simple, high-level summary of where the workflow is in its lifecycle. Will be \"\" (Unknown), \"Pending\", or \"Running\" before the workflow is completed, and \"Succeeded\", \"Failed\" or \"Error\" once the workflow has completed.  # noqa: E501

        :param phase: The phase of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def progress(self):
        """Gets the progress of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Progress to completion  # noqa: E501

        :return: The progress of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Progress to completion  # noqa: E501

        :param progress: The progress of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def resources_duration(self):
        """Gets the resources_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        ResourcesDuration is the total for the workflow  # noqa: E501

        :return: The resources_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._resources_duration

    @resources_duration.setter
    def resources_duration(self, resources_duration):
        """Sets the resources_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        ResourcesDuration is the total for the workflow  # noqa: E501

        :param resources_duration: The resources_duration of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._resources_duration = resources_duration

    @property
    def started_at(self):
        """Gets the started_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Time at which this workflow started  # noqa: E501

        :return: The started_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Time at which this workflow started  # noqa: E501

        :param started_at: The started_at of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._started_at = started_at

    @property
    def stored_templates(self):
        """Gets the stored_templates of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        StoredTemplates is a mapping between a template ref and the node's status.  # noqa: E501

        :return: The stored_templates of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, IoArgoprojWorkflowV1alpha1Template)
        """
        return self._stored_templates

    @stored_templates.setter
    def stored_templates(self, stored_templates):
        """Sets the stored_templates of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        StoredTemplates is a mapping between a template ref and the node's status.  # noqa: E501

        :param stored_templates: The stored_templates of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, IoArgoprojWorkflowV1alpha1Template)
        """

        self._stored_templates = stored_templates

    @property
    def stored_workflow_template_spec(self):
        """Gets the stored_workflow_template_spec of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        StoredWorkflowSpec stores the WorkflowTemplate spec for future execution.  # noqa: E501

        :return: The stored_workflow_template_spec of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1WorkflowSpec
        """
        return self._stored_workflow_template_spec

    @stored_workflow_template_spec.setter
    def stored_workflow_template_spec(self, stored_workflow_template_spec):
        """Sets the stored_workflow_template_spec of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        StoredWorkflowSpec stores the WorkflowTemplate spec for future execution.  # noqa: E501

        :param stored_workflow_template_spec: The stored_workflow_template_spec of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1WorkflowSpec
        """

        self._stored_workflow_template_spec = stored_workflow_template_spec

    @property
    def synchronization(self):
        """Gets the synchronization of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        Synchronization stores the status of synchronization locks  # noqa: E501

        :return: The synchronization of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1SynchronizationStatus
        """
        return self._synchronization

    @synchronization.setter
    def synchronization(self, synchronization):
        """Sets the synchronization of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        Synchronization stores the status of synchronization locks  # noqa: E501

        :param synchronization: The synchronization of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1SynchronizationStatus
        """

        self._synchronization = synchronization

    @property
    def task_results_completion_status(self):
        """Gets the task_results_completion_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501

        TaskResultsCompletionStatus tracks task result completion status (mapped by node ID). Used to prevent premature archiving and garbage collection.  # noqa: E501

        :return: The task_results_completion_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._task_results_completion_status

    @task_results_completion_status.setter
    def task_results_completion_status(self, task_results_completion_status):
        """Sets the task_results_completion_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.

        TaskResultsCompletionStatus tracks task result completion status (mapped by node ID). Used to prevent premature archiving and garbage collection.  # noqa: E501

        :param task_results_completion_status: The task_results_completion_status of this IoArgoprojWorkflowV1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, bool)
        """

        self._task_results_completion_status = task_results_completion_status

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
        if issubclass(IoArgoprojWorkflowV1alpha1WorkflowStatus, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowStatus):
            return True

        return self.to_dict() != other.to_dict()
