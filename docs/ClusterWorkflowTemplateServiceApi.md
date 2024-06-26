# swagger_client.ClusterWorkflowTemplateServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_workflow_template_service_create_cluster_workflow_template**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_create_cluster_workflow_template) | **POST** /api/v1/cluster-workflow-templates | 
[**cluster_workflow_template_service_delete_cluster_workflow_template**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_delete_cluster_workflow_template) | **DELETE** /api/v1/cluster-workflow-templates/{name} | 
[**cluster_workflow_template_service_get_cluster_workflow_template**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_get_cluster_workflow_template) | **GET** /api/v1/cluster-workflow-templates/{name} | 
[**cluster_workflow_template_service_lint_cluster_workflow_template**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_lint_cluster_workflow_template) | **POST** /api/v1/cluster-workflow-templates/lint | 
[**cluster_workflow_template_service_list_cluster_workflow_templates**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_list_cluster_workflow_templates) | **GET** /api/v1/cluster-workflow-templates | 
[**cluster_workflow_template_service_update_cluster_workflow_template**](ClusterWorkflowTemplateServiceApi.md#cluster_workflow_template_service_update_cluster_workflow_template) | **PUT** /api/v1/cluster-workflow-templates/{name} | 


# **cluster_workflow_template_service_create_cluster_workflow_template**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate cluster_workflow_template_service_create_cluster_workflow_template(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest() # IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest | 

try:
    api_response = api_instance.cluster_workflow_template_service_create_cluster_workflow_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_create_cluster_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateCreateRequest.md)|  | 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_workflow_template_service_delete_cluster_workflow_template**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateDeleteResponse cluster_workflow_template_service_delete_cluster_workflow_template(name, delete_options_grace_period_seconds=delete_options_grace_period_seconds, delete_options_preconditions_uid=delete_options_preconditions_uid, delete_options_preconditions_resource_version=delete_options_preconditions_resource_version, delete_options_orphan_dependents=delete_options_orphan_dependents, delete_options_propagation_policy=delete_options_propagation_policy, delete_options_dry_run=delete_options_dry_run)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
delete_options_grace_period_seconds = 'delete_options_grace_period_seconds_example' # str | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. +optional. (optional)
delete_options_preconditions_uid = 'delete_options_preconditions_uid_example' # str | Specifies the target UID. +optional. (optional)
delete_options_preconditions_resource_version = 'delete_options_preconditions_resource_version_example' # str | Specifies the target ResourceVersion +optional. (optional)
delete_options_orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. +optional. (optional)
delete_options_propagation_policy = 'delete_options_propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. +optional. (optional)
delete_options_dry_run = ['delete_options_dry_run_example'] # list[str] | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed +optional. (optional)

try:
    api_response = api_instance.cluster_workflow_template_service_delete_cluster_workflow_template(name, delete_options_grace_period_seconds=delete_options_grace_period_seconds, delete_options_preconditions_uid=delete_options_preconditions_uid, delete_options_preconditions_resource_version=delete_options_preconditions_resource_version, delete_options_orphan_dependents=delete_options_orphan_dependents, delete_options_propagation_policy=delete_options_propagation_policy, delete_options_dry_run=delete_options_dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_delete_cluster_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **delete_options_grace_period_seconds** | **str**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. +optional. | [optional] 
 **delete_options_preconditions_uid** | **str**| Specifies the target UID. +optional. | [optional] 
 **delete_options_preconditions_resource_version** | **str**| Specifies the target ResourceVersion +optional. | [optional] 
 **delete_options_orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. +optional. | [optional] 
 **delete_options_propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. +optional. | [optional] 
 **delete_options_dry_run** | [**list[str]**](str.md)| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed +optional. | [optional] 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateDeleteResponse**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateDeleteResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_workflow_template_service_get_cluster_workflow_template**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate cluster_workflow_template_service_get_cluster_workflow_template(name, get_options_resource_version=get_options_resource_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
get_options_resource_version = 'get_options_resource_version_example' # str | resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional (optional)

try:
    api_response = api_instance.cluster_workflow_template_service_get_cluster_workflow_template(name, get_options_resource_version=get_options_resource_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_get_cluster_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **get_options_resource_version** | **str**| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional | [optional] 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_workflow_template_service_lint_cluster_workflow_template**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate cluster_workflow_template_service_lint_cluster_workflow_template(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest() # IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest | 

try:
    api_response = api_instance.cluster_workflow_template_service_lint_cluster_workflow_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_lint_cluster_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateLintRequest.md)|  | 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_workflow_template_service_list_cluster_workflow_templates**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList cluster_workflow_template_service_list_cluster_workflow_templates(list_options_label_selector=list_options_label_selector, list_options_field_selector=list_options_field_selector, list_options_watch=list_options_watch, list_options_allow_watch_bookmarks=list_options_allow_watch_bookmarks, list_options_resource_version=list_options_resource_version, list_options_resource_version_match=list_options_resource_version_match, list_options_timeout_seconds=list_options_timeout_seconds, list_options_limit=list_options_limit, list_options_continue=list_options_continue)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
list_options_label_selector = 'list_options_label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional. (optional)
list_options_field_selector = 'list_options_field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional. (optional)
list_options_watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional. (optional)
list_options_allow_watch_bookmarks = true # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. +optional. (optional)
list_options_resource_version = 'list_options_resource_version_example' # str | resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional (optional)
list_options_resource_version_match = 'list_options_resource_version_match_example' # str | resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional (optional)
list_options_timeout_seconds = 'list_options_timeout_seconds_example' # str | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional. (optional)
list_options_limit = 'list_options_limit_example' # str | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
list_options_continue = 'list_options_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)

try:
    api_response = api_instance.cluster_workflow_template_service_list_cluster_workflow_templates(list_options_label_selector=list_options_label_selector, list_options_field_selector=list_options_field_selector, list_options_watch=list_options_watch, list_options_allow_watch_bookmarks=list_options_allow_watch_bookmarks, list_options_resource_version=list_options_resource_version, list_options_resource_version_match=list_options_resource_version_match, list_options_timeout_seconds=list_options_timeout_seconds, list_options_limit=list_options_limit, list_options_continue=list_options_continue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_list_cluster_workflow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_options_label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional. | [optional] 
 **list_options_field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional. | [optional] 
 **list_options_watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional. | [optional] 
 **list_options_allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. +optional. | [optional] 
 **list_options_resource_version** | **str**| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional | [optional] 
 **list_options_resource_version_match** | **str**| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional | [optional] 
 **list_options_timeout_seconds** | **str**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional. | [optional] 
 **list_options_limit** | **str**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **list_options_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_workflow_template_service_update_cluster_workflow_template**
> IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate cluster_workflow_template_service_update_cluster_workflow_template(name, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ClusterWorkflowTemplateServiceApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | DEPRECATED: This field is ignored.
body = swagger_client.IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest() # IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest | 

try:
    api_response = api_instance.cluster_workflow_template_service_update_cluster_workflow_template(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterWorkflowTemplateServiceApi->cluster_workflow_template_service_update_cluster_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| DEPRECATED: This field is ignored. | 
 **body** | [**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplateUpdateRequest.md)|  | 

### Return type

[**IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate**](IoArgoprojWorkflowV1alpha1ClusterWorkflowTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

