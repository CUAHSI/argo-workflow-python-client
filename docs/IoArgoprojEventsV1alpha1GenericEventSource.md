# IoArgoprojEventsV1alpha1GenericEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 
**config** | **str** |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**insecure** | **bool** | Insecure determines the type of connection. | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**url** | **str** | URL of the gRPC server that implements the event source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


