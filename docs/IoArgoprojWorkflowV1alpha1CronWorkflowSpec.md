# IoArgoprojWorkflowV1alpha1CronWorkflowSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency_policy** | **str** | ConcurrencyPolicy is the K8s-style concurrency policy that will be used | [optional] 
**failed_jobs_history_limit** | **int** | FailedJobsHistoryLimit is the number of failed jobs to be kept at a time | [optional] 
**schedule** | **str** | Schedule is a schedule to run the Workflow in Cron format | 
**starting_deadline_seconds** | **int** | StartingDeadlineSeconds is the K8s-style deadline that will limit the time a CronWorkflow will be run after its original scheduled time if it is missed. | [optional] 
**successful_jobs_history_limit** | **int** | SuccessfulJobsHistoryLimit is the number of successful jobs to be kept at a time | [optional] 
**suspend** | **bool** | Suspend is a flag that will stop new CronWorkflows from running if set to true | [optional] 
**timezone** | **str** | Timezone is the timezone against which the cron schedule will be calculated, e.g. \&quot;Asia/Tokyo\&quot;. Default is machine&#39;s local time. | [optional] 
**workflow_metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | WorkflowMetadata contains some metadata of the workflow to be run | [optional] 
**workflow_spec** | [**IoArgoprojWorkflowV1alpha1WorkflowSpec**](IoArgoprojWorkflowV1alpha1WorkflowSpec.md) | WorkflowSpec is the spec of the workflow to be run | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


