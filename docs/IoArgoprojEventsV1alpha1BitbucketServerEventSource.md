# IoArgoprojEventsV1alpha1BitbucketServerEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 
**bitbucketserver_base_url** | **str** |  | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**events** | **list[str]** |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**project_key** | **str** |  | [optional] 
**repositories** | [**list[IoArgoprojEventsV1alpha1BitbucketServerRepository]**](IoArgoprojEventsV1alpha1BitbucketServerRepository.md) |  | [optional] 
**repository_slug** | **str** |  | [optional] 
**webhook** | [**IoArgoprojEventsV1alpha1WebhookContext**](IoArgoprojEventsV1alpha1WebhookContext.md) |  | [optional] 
**webhook_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


