# or_rest_client.MapApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_map**](MapApi.md#delete_map) | **DELETE** /map/deleteMap | Removes mbtiles file
[**get_custom_map_info**](MapApi.md#get_custom_map_info) | **GET** /map/getCustomMapInfo | Retrieve if the map is custom and custom map limit
[**get_settings**](MapApi.md#get_settings) | **GET** /map | Retrieve the style used for Mapbox GL
[**get_settings_js**](MapApi.md#get_settings_js) | **GET** /map/js | Retrieve the tileJSON object used for Mapbox GL
[**get_tile**](MapApi.md#get_tile) | **GET** /map/tile/{zoom}/{column}/{row} | Retrieve the vector tile data for Mapbox GL
[**save_settings**](MapApi.md#save_settings) | **PUT** /map | Update map settings
[**upload_map**](MapApi.md#upload_map) | **POST** /map/upload | Saves mbtiles file


# **delete_map**
> object delete_map(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Removes mbtiles file

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Removes mbtiles file
    api_response = api_instance.delete_map(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of MapApi->delete_map:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->delete_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

**object**

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

# **get_custom_map_info**
> object get_custom_map_info()

Retrieve if the map is custom and custom map limit

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)

try:
    # Retrieve if the map is custom and custom map limit
    api_response = api_instance.get_custom_map_info()
    print("The response of MapApi->get_custom_map_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->get_custom_map_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **get_settings**
> object get_settings(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the style used for Mapbox GL

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the style used for Mapbox GL
    api_response = api_instance.get_settings(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of MapApi->get_settings:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->get_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

**object**

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

# **get_settings_js**
> object get_settings_js(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the tileJSON object used for Mapbox GL

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the tileJSON object used for Mapbox GL
    api_response = api_instance.get_settings_js(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of MapApi->get_settings_js:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->get_settings_js: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

**object**

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

# **get_tile**
> bytearray get_tile(zoom, column, row)

Retrieve the vector tile data for Mapbox GL

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
zoom = 56 # int | 
column = 56 # int | 
row = 56 # int | 

try:
    # Retrieve the vector tile data for Mapbox GL
    api_response = api_instance.get_tile(zoom, column, row)
    print("The response of MapApi->get_tile:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->get_tile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoom** | **int**|  | 
 **column** | **int**|  | 
 **row** | **int**|  | 

### Return type

**bytearray**

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mapbox-vector-tile

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_settings**
> object save_settings(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, map_config=map_config)

Update map settings

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.models.map_config import MapConfig
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
map_config = or_rest_client.MapConfig() # MapConfig |  (optional)

try:
    # Update map settings
    api_response = api_instance.save_settings(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, map_config=map_config)
    print("The response of MapApi->save_settings:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->save_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **map_config** | [**MapConfig**](MapConfig.md)|  | [optional] 

### Return type

**object**

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

# **upload_map**
> object upload_map(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, filename=filename)

Saves mbtiles file

### Example


```python
from or_rest_client import AuthenticatedApiClient, MapApi
from or_rest_client.rest import ApiException
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
api_instance = MapApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    # Saves mbtiles file
    api_response = api_instance.upload_map(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, filename=filename)
    print("The response of MapApi->upload_map:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling MapApi->upload_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

**object**

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

