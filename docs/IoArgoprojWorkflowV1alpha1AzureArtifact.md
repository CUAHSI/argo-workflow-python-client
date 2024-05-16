# IoArgoprojWorkflowV1alpha1AzureArtifact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) | AccountKeySecret is the secret selector to the Azure Blob Storage account access key | [optional] 
**blob** | **str** | Blob is the blob name (i.e., path) in the container where the artifact resides | 
**container** | **str** | Container is the container where resources will be stored | 
**endpoint** | **str** | Endpoint is the service url associated with an account. It is most likely \&quot;https://&lt;ACCOUNT_NAME&gt;.blob.core.windows.net\&quot; | 
**use_sdk_creds** | **bool** | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


