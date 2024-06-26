# IoArgoprojWorkflowV1alpha1Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default is the default value to use for an input parameter if a value was not supplied | [optional] 
**description** | **str** | Description is the parameter description | [optional] 
**enum** | **list[str]** | Enum holds a list of string values to choose from, for the actual value of the parameter | [optional] 
**global_name** | **str** | GlobalName exports an output parameter to the global scope, making it available as &#39;{{io.argoproj.workflow.v1alpha1.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters | [optional] 
**name** | **str** | Name is the parameter name | 
**value** | **str** | Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values | [optional] 
**value_from** | [**IoArgoprojWorkflowV1alpha1ValueFrom**](IoArgoprojWorkflowV1alpha1ValueFrom.md) | ValueFrom is the source for the output parameter&#39;s value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


