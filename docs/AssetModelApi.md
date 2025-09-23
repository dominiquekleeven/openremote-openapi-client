# openremote_openapi_client.AssetModelApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_descriptors**](AssetModelApi.md#get_asset_descriptors) | **GET** /model/assetDescriptors | Retrieve the available asset descriptors
[**get_asset_info**](AssetModelApi.md#get_asset_info) | **GET** /model/assetInfo/{assetType} | Retrieve the asset type information of an asset type
[**get_asset_infos**](AssetModelApi.md#get_asset_infos) | **GET** /model/assetInfos | Retrieve the asset type information of each available asset type
[**get_meta_item_descriptors**](AssetModelApi.md#get_meta_item_descriptors) | **GET** /model/metaItemDescriptors | Retrieve the available meta item descriptors
[**get_value_descriptors**](AssetModelApi.md#get_value_descriptors) | **GET** /model/valueDescriptors | Retrieve the available value descriptors


# **get_asset_descriptors**
> List[AssetDescriptorObject] get_asset_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, parent_type=parent_type)

Retrieve the available asset descriptors

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, AssetModelApi
from openremote_openapi_client.models.asset_descriptor_object import AssetDescriptorObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create authenticated client for OpenRemote
client = AuthenticatedApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetModelApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)
parent_type = 'parent_type_example' # str |  (optional)

try:
    # Retrieve the available asset descriptors
    api_response = api_instance.get_asset_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, parent_type=parent_type)
    print("The response of AssetModelApi->get_asset_descriptors:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetModelApi->get_asset_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **parent_type** | **str**|  | [optional] 

### Return type

[**List[AssetDescriptorObject]**](AssetDescriptorObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_info**
> AssetTypeInfo get_asset_info(asset_type, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)

Retrieve the asset type information of an asset type

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, AssetModelApi
from openremote_openapi_client.models.asset_type_info import AssetTypeInfo
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create authenticated client for OpenRemote
client = AuthenticatedApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetModelApi(client)
asset_type = 'asset_type_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)

try:
    # Retrieve the asset type information of an asset type
    api_response = api_instance.get_asset_info(asset_type, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)
    print("The response of AssetModelApi->get_asset_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetModelApi->get_asset_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 

### Return type

[**AssetTypeInfo**](AssetTypeInfo.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_infos**
> List[AssetTypeInfo] get_asset_infos(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, parent_type=parent_type)

Retrieve the asset type information of each available asset type

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, AssetModelApi
from openremote_openapi_client.models.asset_type_info import AssetTypeInfo
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create authenticated client for OpenRemote
client = AuthenticatedApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetModelApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)
parent_type = 'parent_type_example' # str |  (optional)

try:
    # Retrieve the asset type information of each available asset type
    api_response = api_instance.get_asset_infos(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, parent_type=parent_type)
    print("The response of AssetModelApi->get_asset_infos:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetModelApi->get_asset_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **parent_type** | **str**|  | [optional] 

### Return type

[**List[AssetTypeInfo]**](AssetTypeInfo.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_item_descriptors**
> Dict[str, MetaItemDescriptorObject] get_meta_item_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)

Retrieve the available meta item descriptors

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, AssetModelApi
from openremote_openapi_client.models.meta_item_descriptor_object import MetaItemDescriptorObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create authenticated client for OpenRemote
client = AuthenticatedApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetModelApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)

try:
    # Retrieve the available meta item descriptors
    api_response = api_instance.get_meta_item_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)
    print("The response of AssetModelApi->get_meta_item_descriptors:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetModelApi->get_meta_item_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 

### Return type

[**Dict[str, MetaItemDescriptorObject]**](MetaItemDescriptorObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_value_descriptors**
> Dict[str, ValueDescriptorObject] get_value_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)

Retrieve the available value descriptors

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, AssetModelApi
from openremote_openapi_client.models.value_descriptor_object import ValueDescriptorObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create authenticated client for OpenRemote
client = AuthenticatedApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetModelApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)

try:
    # Retrieve the available value descriptors
    api_response = api_instance.get_value_descriptors(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id)
    print("The response of AssetModelApi->get_value_descriptors:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetModelApi->get_value_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 

### Return type

[**Dict[str, ValueDescriptorObject]**](ValueDescriptorObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

