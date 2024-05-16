# swagger_client.InfoServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_service_collect_event**](InfoServiceApi.md#info_service_collect_event) | **POST** /api/v1/tracking/event | 
[**info_service_get_info**](InfoServiceApi.md#info_service_get_info) | **GET** /api/v1/info | 
[**info_service_get_user_info**](InfoServiceApi.md#info_service_get_user_info) | **GET** /api/v1/userinfo | 
[**info_service_get_version**](InfoServiceApi.md#info_service_get_version) | **GET** /api/v1/version | 


# **info_service_collect_event**
> IoArgoprojWorkflowV1alpha1CollectEventResponse info_service_collect_event(body)



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
api_instance = swagger_client.InfoServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.IoArgoprojWorkflowV1alpha1CollectEventRequest() # IoArgoprojWorkflowV1alpha1CollectEventRequest | 

try:
    api_response = api_instance.info_service_collect_event(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->info_service_collect_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoArgoprojWorkflowV1alpha1CollectEventRequest**](IoArgoprojWorkflowV1alpha1CollectEventRequest.md)|  | 

### Return type

[**IoArgoprojWorkflowV1alpha1CollectEventResponse**](IoArgoprojWorkflowV1alpha1CollectEventResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_service_get_info**
> IoArgoprojWorkflowV1alpha1InfoResponse info_service_get_info()



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
api_instance = swagger_client.InfoServiceApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.info_service_get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->info_service_get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoArgoprojWorkflowV1alpha1InfoResponse**](IoArgoprojWorkflowV1alpha1InfoResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_service_get_user_info**
> IoArgoprojWorkflowV1alpha1GetUserInfoResponse info_service_get_user_info()



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
api_instance = swagger_client.InfoServiceApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.info_service_get_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->info_service_get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoArgoprojWorkflowV1alpha1GetUserInfoResponse**](IoArgoprojWorkflowV1alpha1GetUserInfoResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_service_get_version**
> IoArgoprojWorkflowV1alpha1Version info_service_get_version()



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
api_instance = swagger_client.InfoServiceApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.info_service_get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoServiceApi->info_service_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoArgoprojWorkflowV1alpha1Version**](IoArgoprojWorkflowV1alpha1Version.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

