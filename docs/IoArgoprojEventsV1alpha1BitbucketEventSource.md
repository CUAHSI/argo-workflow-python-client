# IoArgoprojEventsV1alpha1BitbucketEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoArgoprojEventsV1alpha1BitbucketAuth**](IoArgoprojEventsV1alpha1BitbucketAuth.md) | Auth information required to connect to Bitbucket. | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**events** | **list[str]** | Events this webhook is subscribed to. | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**owner** | **str** |  | [optional] 
**project_key** | **str** |  | [optional] 
**repositories** | [**list[IoArgoprojEventsV1alpha1BitbucketRepository]**](IoArgoprojEventsV1alpha1BitbucketRepository.md) |  | [optional] 
**repository_slug** | **str** |  | [optional] 
**webhook** | [**IoArgoprojEventsV1alpha1WebhookContext**](IoArgoprojEventsV1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


