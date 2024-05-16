# IoArgoprojWorkflowV1alpha1HTTP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body is content of the HTTP Request | [optional] 
**body_from** | [**IoArgoprojWorkflowV1alpha1HTTPBodySource**](IoArgoprojWorkflowV1alpha1HTTPBodySource.md) | BodyFrom is  content of the HTTP Request as Bytes | [optional] 
**headers** | [**list[IoArgoprojWorkflowV1alpha1HTTPHeader]**](IoArgoprojWorkflowV1alpha1HTTPHeader.md) | Headers are an optional list of headers to send with HTTP requests | [optional] 
**insecure_skip_verify** | **bool** | InsecureSkipVerify is a bool when if set to true will skip TLS verification for the HTTP client | [optional] 
**method** | **str** | Method is HTTP methods for HTTP Request | [optional] 
**success_condition** | **str** | SuccessCondition is an expression if evaluated to true is considered successful | [optional] 
**timeout_seconds** | **int** | TimeoutSeconds is request timeout for HTTP Request. Default is 30 seconds | [optional] 
**url** | **str** | URL of the HTTP Request | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


