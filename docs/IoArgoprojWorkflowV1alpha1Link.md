# IoArgoprojWorkflowV1alpha1Link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the link, E.g. \&quot;Workflow Logs\&quot; or \&quot;Pod Logs\&quot; | 
**scope** | **str** | \&quot;workflow\&quot;, \&quot;pod\&quot;, \&quot;pod-logs\&quot;, \&quot;event-source-logs\&quot;, \&quot;sensor-logs\&quot;, \&quot;workflow-list\&quot; or \&quot;chat\&quot; | 
**url** | **str** | The URL. Can contain \&quot;${metadata.namespace}\&quot;, \&quot;${metadata.name}\&quot;, \&quot;${status.startedAt}\&quot;, \&quot;${status.finishedAt}\&quot; or any other element in workflow yaml, e.g. \&quot;${io.argoproj.workflow.v1alpha1.metadata.annotations.userDefinedKey}\&quot; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


