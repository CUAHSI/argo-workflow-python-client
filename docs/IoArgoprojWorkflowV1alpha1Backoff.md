# IoArgoprojWorkflowV1alpha1Backoff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Duration is the amount to back off. Default unit is seconds, but could also be a duration (e.g. \&quot;2m\&quot;, \&quot;1h\&quot;) | [optional] 
**factor** | [**IoK8sApimachineryPkgUtilIntstrIntOrString**](IoK8sApimachineryPkgUtilIntstrIntOrString.md) | Factor is a factor to multiply the base duration after each failed retry | [optional] 
**max_duration** | **str** | MaxDuration is the maximum amount of time allowed for a workflow in the backoff strategy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


