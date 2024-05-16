# IoArgoprojWorkflowV1alpha1ContainerSetTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**list[IoArgoprojWorkflowV1alpha1ContainerNode]**](IoArgoprojWorkflowV1alpha1ContainerNode.md) |  | 
**retry_strategy** | [**IoArgoprojWorkflowV1alpha1ContainerSetRetryStrategy**](IoArgoprojWorkflowV1alpha1ContainerSetRetryStrategy.md) | RetryStrategy describes how to retry a container nodes in the container set if it fails. Nbr of retries(default 0) and sleep duration between retries(default 0s, instant retry) can be set. | [optional] 
**volume_mounts** | [**list[IoK8sApiCoreV1VolumeMount]**](IoK8sApiCoreV1VolumeMount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


