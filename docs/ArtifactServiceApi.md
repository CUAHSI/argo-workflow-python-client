# swagger_client.ArtifactServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifact_service_get_artifact_file**](ArtifactServiceApi.md#artifact_service_get_artifact_file) | **GET** /artifact-files/{namespace}/{idDiscriminator}/{id}/{nodeId}/{artifactDiscriminator}/{artifactName} | Get an artifact.
[**artifact_service_get_input_artifact**](ArtifactServiceApi.md#artifact_service_get_input_artifact) | **GET** /input-artifacts/{namespace}/{name}/{nodeId}/{artifactName} | Get an input artifact.
[**artifact_service_get_input_artifact_by_uid**](ArtifactServiceApi.md#artifact_service_get_input_artifact_by_uid) | **GET** /input-artifacts-by-uid/{uid}/{nodeId}/{artifactName} | Get an input artifact by UID.
[**artifact_service_get_output_artifact**](ArtifactServiceApi.md#artifact_service_get_output_artifact) | **GET** /artifacts/{namespace}/{name}/{nodeId}/{artifactName} | Get an output artifact.
[**artifact_service_get_output_artifact_by_uid**](ArtifactServiceApi.md#artifact_service_get_output_artifact_by_uid) | **GET** /artifacts-by-uid/{uid}/{nodeId}/{artifactName} | Get an output artifact by UID.


# **artifact_service_get_artifact_file**
> str artifact_service_get_artifact_file(namespace, id_discriminator, id, node_id, artifact_name, artifact_discriminator)

Get an artifact.

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
api_instance = swagger_client.ArtifactServiceApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
id_discriminator = 'id_discriminator_example' # str | 
id = 'id_example' # str | 
node_id = 'node_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 
artifact_discriminator = 'artifact_discriminator_example' # str | 

try:
    # Get an artifact.
    api_response = api_instance.artifact_service_get_artifact_file(namespace, id_discriminator, id, node_id, artifact_name, artifact_discriminator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactServiceApi->artifact_service_get_artifact_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **id_discriminator** | **str**|  | 
 **id** | **str**|  | 
 **node_id** | **str**|  | 
 **artifact_name** | **str**|  | 
 **artifact_discriminator** | **str**|  | 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_service_get_input_artifact**
> str artifact_service_get_input_artifact(namespace, name, node_id, artifact_name)

Get an input artifact.

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
api_instance = swagger_client.ArtifactServiceApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
node_id = 'node_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 

try:
    # Get an input artifact.
    api_response = api_instance.artifact_service_get_input_artifact(namespace, name, node_id, artifact_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactServiceApi->artifact_service_get_input_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **node_id** | **str**|  | 
 **artifact_name** | **str**|  | 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_service_get_input_artifact_by_uid**
> str artifact_service_get_input_artifact_by_uid(uid, node_id, artifact_name)

Get an input artifact by UID.

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
api_instance = swagger_client.ArtifactServiceApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 
node_id = 'node_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 

try:
    # Get an input artifact by UID.
    api_response = api_instance.artifact_service_get_input_artifact_by_uid(uid, node_id, artifact_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactServiceApi->artifact_service_get_input_artifact_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **node_id** | **str**|  | 
 **artifact_name** | **str**|  | 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_service_get_output_artifact**
> str artifact_service_get_output_artifact(namespace, name, node_id, artifact_name)

Get an output artifact.

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
api_instance = swagger_client.ArtifactServiceApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
node_id = 'node_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 

try:
    # Get an output artifact.
    api_response = api_instance.artifact_service_get_output_artifact(namespace, name, node_id, artifact_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactServiceApi->artifact_service_get_output_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **node_id** | **str**|  | 
 **artifact_name** | **str**|  | 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_service_get_output_artifact_by_uid**
> str artifact_service_get_output_artifact_by_uid(uid, node_id, artifact_name)

Get an output artifact by UID.

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
api_instance = swagger_client.ArtifactServiceApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 
node_id = 'node_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 

try:
    # Get an output artifact by UID.
    api_response = api_instance.artifact_service_get_output_artifact_by_uid(uid, node_id, artifact_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactServiceApi->artifact_service_get_output_artifact_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **node_id** | **str**|  | 
 **artifact_name** | **str**|  | 

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

