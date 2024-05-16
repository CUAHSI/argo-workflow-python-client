# IoArgoprojEventsV1alpha1Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**IoK8sApiCoreV1Affinity**](IoK8sApiCoreV1Affinity.md) |  | [optional] 
**container** | [**IoK8sApiCoreV1Container**](IoK8sApiCoreV1Container.md) |  | [optional] 
**image_pull_secrets** | [**list[IoK8sApiCoreV1LocalObjectReference]**](IoK8sApiCoreV1LocalObjectReference.md) |  | [optional] 
**metadata** | [**IoArgoprojEventsV1alpha1Metadata**](IoArgoprojEventsV1alpha1Metadata.md) |  | [optional] 
**node_selector** | **dict(str, str)** |  | [optional] 
**priority** | **int** |  | [optional] 
**priority_class_name** | **str** |  | [optional] 
**security_context** | [**IoK8sApiCoreV1PodSecurityContext**](IoK8sApiCoreV1PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** |  | [optional] 
**tolerations** | [**list[IoK8sApiCoreV1Toleration]**](IoK8sApiCoreV1Toleration.md) |  | [optional] 
**volumes** | [**list[IoK8sApiCoreV1Volume]**](IoK8sApiCoreV1Volume.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


