# IoArgoprojWorkflowV1alpha1PodGC

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_delay_duration** | [**IoK8sApimachineryPkgApisMetaV1Duration**](IoK8sApimachineryPkgApisMetaV1Duration.md) | DeleteDelayDuration specifies the duration before pods in the GC queue get deleted. | [optional] 
**label_selector** | [**IoK8sApimachineryPkgApisMetaV1LabelSelector**](IoK8sApimachineryPkgApisMetaV1LabelSelector.md) | LabelSelector is the label selector to check if the pods match the labels before being added to the pod GC queue. | [optional] 
**strategy** | **str** | Strategy is the strategy to use. One of \&quot;OnPodCompletion\&quot;, \&quot;OnPodSuccess\&quot;, \&quot;OnWorkflowCompletion\&quot;, \&quot;OnWorkflowSuccess\&quot;. If unset, does not delete Pods | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


