# IoArgoprojWorkflowV1alpha1ResourceTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action is the action to perform to the resource. Must be one of: get, create, apply, delete, replace, patch | 
**failure_condition** | **str** | FailureCondition is a label selector expression which describes the conditions of the k8s resource in which the step was considered failed | [optional] 
**flags** | **list[str]** | Flags is a set of additional options passed to kubectl before submitting a resource I.e. to disable resource validation: flags: [  \&quot;--validate&#x3D;false\&quot;  # disable resource validation ] | [optional] 
**manifest** | **str** | Manifest contains the kubernetes manifest | [optional] 
**manifest_from** | [**IoArgoprojWorkflowV1alpha1ManifestFrom**](IoArgoprojWorkflowV1alpha1ManifestFrom.md) | ManifestFrom is the source for a single kubernetes manifest | [optional] 
**merge_strategy** | **str** | MergeStrategy is the strategy used to merge a patch. It defaults to \&quot;strategic\&quot; Must be one of: strategic, merge, json | [optional] 
**set_owner_reference** | **bool** | SetOwnerReference sets the reference to the workflow on the OwnerReference of generated resource. | [optional] 
**success_condition** | **str** | SuccessCondition is a label selector expression which describes the conditions of the k8s resource in which it is acceptable to proceed to the following step | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


