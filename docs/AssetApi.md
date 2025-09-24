# openremote_openapi_client.AssetApi

**[Official OpenRemote REST API Docs](https://docs.openremote.io/docs/category/rest-api)**

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetApi.md#create_asset) | **POST** /asset | Create an asset
[**create_user_asset_links**](AssetApi.md#create_user_asset_links) | **POST** /asset/user/link | Create links between users and assets
[**delete_all_user_asset_links**](AssetApi.md#delete_all_user_asset_links) | **DELETE** /asset/user/link/{realm}/{userId} | Delete all user asset links
[**delete_asset**](AssetApi.md#delete_asset) | **DELETE** /asset | Delete assets
[**delete_assets_parent**](AssetApi.md#delete_assets_parent) | **DELETE** /asset/parent | Delete the parent of assets
[**delete_user_asset_link**](AssetApi.md#delete_user_asset_link) | **DELETE** /asset/user/link/{realm}/{userId}/{assetId} | Delete a link between an asset and user
[**delete_user_asset_links**](AssetApi.md#delete_user_asset_links) | **POST** /asset/user/link/delete | Delete user asset links
[**get_asset**](AssetApi.md#get_asset) | **GET** /asset/{assetId} | Retrieve an asset
[**get_current_user_assets**](AssetApi.md#get_current_user_assets) | **GET** /asset/user/current | Retrieve the linked assets of the currently authenticated user
[**get_partial_asset**](AssetApi.md#get_partial_asset) | **GET** /asset/partial/{assetId} | Retrieve a partially loaded asset (no attributes or path)
[**get_user_asset_links**](AssetApi.md#get_user_asset_links) | **GET** /asset/user/link | Retrieve links between assets and users
[**query_assets**](AssetApi.md#query_assets) | **POST** /asset/query | Retrieve assets using a query
[**update_asset**](AssetApi.md#update_asset) | **PUT** /asset/{assetId} | Update an asset
[**update_asset_parent**](AssetApi.md#update_asset_parent) | **PUT** /asset/{parentAssetId}/child | Update the parent of assets
[**write_attribute_events**](AssetApi.md#write_attribute_events) | **PUT** /asset/attributes/timestamp | Update attribute values with timestamps
[**write_attribute_value**](AssetApi.md#write_attribute_value) | **PUT** /asset/{assetId}/attribute/{attributeName} | Write to a single attribute
[**write_attribute_value1**](AssetApi.md#write_attribute_value1) | **PUT** /asset/{assetId}/attribute/{attributeName}/{timestamp} | Write to a single attribute with a timestamp
[**write_attribute_values**](AssetApi.md#write_attribute_values) | **PUT** /asset/attributes | Update attribute values


# **create_asset**
> AssetObject create_asset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_object=asset_object)

Create an asset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_object = AssetObject() # AssetObject |  (optional)

try:
    # Create an asset
    api_response = api_instance.create_asset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_object=asset_object)
    print("The response of AssetApi->create_asset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->create_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_object** | [**AssetObject**](AssetObject.md)|  | [optional] 

### Return type

[**AssetObject**](AssetObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_asset_links**
> create_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, user_asset_link=user_asset_link)

Create links between users and assets

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.user_asset_link import UserAssetLink
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
user_asset_link = [openremote_openapi_client.UserAssetLink()] # List[UserAssetLink] |  (optional)

try:
    # Create links between users and assets
    api_instance.create_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, user_asset_link=user_asset_link)
except Exception as e:
    print("Exception when calling AssetApi->create_user_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **user_asset_link** | [**List[UserAssetLink]**](UserAssetLink.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_user_asset_links**
> delete_all_user_asset_links(realm, user_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete all user asset links

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
realm = 'realm_example' # str | 
user_id = 'user_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete all user asset links
    api_instance.delete_all_user_asset_links(realm, user_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AssetApi->delete_all_user_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **user_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **delete_asset**
> delete_asset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_id=asset_id)

Delete assets

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_id = ['asset_id_example'] # List[str] |  (optional)

try:
    # Delete assets
    api_instance.delete_asset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_id=asset_id)
except Exception as e:
    print("Exception when calling AssetApi->delete_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_id** | [**List[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

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

# **delete_assets_parent**
> delete_assets_parent(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)

Delete the parent of assets

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_ids = ['asset_ids_example'] # List[str] |  (optional)

try:
    # Delete the parent of assets
    api_instance.delete_assets_parent(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)
except Exception as e:
    print("Exception when calling AssetApi->delete_assets_parent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

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

# **delete_user_asset_link**
> delete_user_asset_link(realm, user_id, asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a link between an asset and user

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
realm = 'realm_example' # str | 
user_id = 'user_id_example' # str | 
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a link between an asset and user
    api_instance.delete_user_asset_link(realm, user_id, asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AssetApi->delete_user_asset_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **user_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_asset_links**
> delete_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, user_asset_link=user_asset_link)

Delete user asset links

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.user_asset_link import UserAssetLink
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
user_asset_link = [openremote_openapi_client.UserAssetLink()] # List[UserAssetLink] |  (optional)

try:
    # Delete user asset links
    api_instance.delete_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, user_asset_link=user_asset_link)
except Exception as e:
    print("Exception when calling AssetApi->delete_user_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **user_asset_link** | [**List[UserAssetLink]**](UserAssetLink.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetObject get_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve an asset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve an asset
    api_response = api_instance.get_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of AssetApi->get_asset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->get_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**AssetObject**](AssetObject.md)

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

# **get_current_user_assets**
> List[AssetObject] get_current_user_assets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the linked assets of the currently authenticated user

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the linked assets of the currently authenticated user
    api_response = api_instance.get_current_user_assets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of AssetApi->get_current_user_assets:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->get_current_user_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[AssetObject]**](AssetObject.md)

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

# **get_partial_asset**
> AssetObject get_partial_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve a partially loaded asset (no attributes or path)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve a partially loaded asset (no attributes or path)
    api_response = api_instance.get_partial_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of AssetApi->get_partial_asset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->get_partial_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**AssetObject**](AssetObject.md)

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

# **get_user_asset_links**
> List[UserAssetLink] get_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, user_id=user_id, asset_id=asset_id)

Retrieve links between assets and users

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.user_asset_link import UserAssetLink
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
asset_id = 'asset_id_example' # str |  (optional)

try:
    # Retrieve links between assets and users
    api_response = api_instance.get_user_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, user_id=user_id, asset_id=asset_id)
    print("The response of AssetApi->get_user_asset_links:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->get_user_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 

### Return type

[**List[UserAssetLink]**](UserAssetLink.md)

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

# **query_assets**
> List[AssetObject] query_assets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_query=asset_query)

Retrieve assets using a query

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.models.asset_query import AssetQuery
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_query = AssetQuery() # AssetQuery |  (optional)

try:
    # Retrieve assets using a query
    api_response = api_instance.query_assets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_query=asset_query)
    print("The response of AssetApi->query_assets:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->query_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_query** | [**AssetQuery**](AssetQuery.md)|  | [optional] 

### Return type

[**List[AssetObject]**](AssetObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> AssetObject update_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_object=asset_object)

Update an asset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.asset_object import AssetObject
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_object = AssetObject() # AssetObject |  (optional)

try:
    # Update an asset
    api_response = api_instance.update_asset(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_object=asset_object)
    print("The response of AssetApi->update_asset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->update_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_object** | [**AssetObject**](AssetObject.md)|  | [optional] 

### Return type

[**AssetObject**](AssetObject.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_parent**
> update_asset_parent(parent_asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)

Update the parent of assets

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
parent_asset_id = 'parent_asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_ids = ['asset_ids_example'] # List[str] |  (optional)

try:
    # Update the parent of assets
    api_instance.update_asset_parent(parent_asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)
except Exception as e:
    print("Exception when calling AssetApi->update_asset_parent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

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

# **write_attribute_events**
> List[AttributeWriteResult] write_attribute_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, attribute_event=attribute_event)

Update attribute values with timestamps

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.attribute_event import AttributeEvent
from openremote_openapi_client.models.attribute_write_result import AttributeWriteResult
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
attribute_event = [openremote_openapi_client.AttributeEvent()] # List[AttributeEvent] |  (optional)

try:
    # Update attribute values with timestamps
    api_response = api_instance.write_attribute_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, attribute_event=attribute_event)
    print("The response of AssetApi->write_attribute_events:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->write_attribute_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **attribute_event** | [**List[AttributeEvent]**](AttributeEvent.md)|  | [optional] 

### Return type

[**List[AttributeWriteResult]**](AttributeWriteResult.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_attribute_value**
> AttributeWriteResult write_attribute_value(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, body=body)

Write to a single attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.attribute_write_result import AttributeWriteResult
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
asset_id = 'asset_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
body = None # object |  (optional)

try:
    # Write to a single attribute
    api_response = api_instance.write_attribute_value(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, body=body)
    print("The response of AssetApi->write_attribute_value:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->write_attribute_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**AttributeWriteResult**](AttributeWriteResult.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The result of the write operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_attribute_value1**
> AttributeWriteResult write_attribute_value1(asset_id, attribute_name, timestamp, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, body=body)

Write to a single attribute with a timestamp

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.attribute_write_result import AttributeWriteResult
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
asset_id = 'asset_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
timestamp = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
body = None # object |  (optional)

try:
    # Write to a single attribute with a timestamp
    api_response = api_instance.write_attribute_value1(asset_id, attribute_name, timestamp, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, body=body)
    print("The response of AssetApi->write_attribute_value1:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->write_attribute_value1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **timestamp** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**AttributeWriteResult**](AttributeWriteResult.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The result of the write operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_attribute_values**
> List[AttributeWriteResult] write_attribute_values(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, attribute_state=attribute_state)

Update attribute values

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetApi
from openremote_openapi_client.models.attribute_state import AttributeState
from openremote_openapi_client.models.attribute_write_result import AttributeWriteResult
from openremote_openapi_client.rest import ApiException
from pprint import pprint

# Create the OpenRemote Client
client = OpenRemoteApiClient(
    base_url="http://localhost:8080/api/master",
    keycloak_url="http://localhost:8081/auth",
    client_id="serviceuser",
    client_secret="your_secret",
    realm="master"
)

# Create an instance of the API class
api_instance = AssetApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
attribute_state = [openremote_openapi_client.AttributeState()] # List[AttributeState] |  (optional)

try:
    # Update attribute values
    api_response = api_instance.write_attribute_values(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, attribute_state=attribute_state)
    print("The response of AssetApi->write_attribute_values:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetApi->write_attribute_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **attribute_state** | [**List[AttributeState]**](AttributeState.md)|  | [optional] 

### Return type

[**List[AttributeWriteResult]**](AttributeWriteResult.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

