# or_rest_client.ConfigurationApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_upload**](ConfigurationApi.md#file_upload) | **POST** /configuration/manager/file | Upload a file
[**get_manager_config**](ConfigurationApi.md#get_manager_config) | **GET** /configuration/manager | Retrieve the manager configuration JSON
[**get_manager_config_image**](ConfigurationApi.md#get_manager_config_image) | **GET** /configuration/manager/image/{filename} | Retrieve manager configuration images
[**update_configuration**](ConfigurationApi.md#update_configuration) | **PUT** /configuration/manager | Update manager configuration


# **file_upload**
> str file_upload(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, path=path, file_info=file_info)

Upload a file

### Example


```python
from or_rest_client import AuthenticatedApiClient, ConfigurationApi
from or_rest_client.models.file_info import FileInfo
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
api_instance = ConfigurationApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
path = 'path_example' # str |  (optional)
file_info = or_rest_client.FileInfo() # FileInfo |  (optional)

try:
    # Upload a file
    api_response = api_instance.file_upload(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, path=path, file_info=file_info)
    print("The response of ConfigurationApi->file_upload:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConfigurationApi->file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **file_info** | [**FileInfo**](FileInfo.md)|  | [optional] 

### Return type

**str**

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

# **get_manager_config**
> ManagerAppConfig get_manager_config()

Retrieve the manager configuration JSON

### Example


```python
from or_rest_client import AuthenticatedApiClient, ConfigurationApi
from or_rest_client.models.manager_app_config import ManagerAppConfig
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
api_instance = ConfigurationApi(client)

try:
    # Retrieve the manager configuration JSON
    api_response = api_instance.get_manager_config()
    print("The response of ConfigurationApi->get_manager_config:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConfigurationApi->get_manager_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManagerAppConfig**](ManagerAppConfig.md)

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

# **get_manager_config_image**
> object get_manager_config_image(filename)

Retrieve manager configuration images

### Example


```python
from or_rest_client import AuthenticatedApiClient, ConfigurationApi
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
api_instance = ConfigurationApi(client)
filename = 'filename_example' # str | 

try:
    # Retrieve manager configuration images
    api_response = api_instance.get_manager_config_image(filename)
    print("The response of ConfigurationApi->get_manager_config_image:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConfigurationApi->get_manager_config_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

**object**

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

# **update_configuration**
> ManagerAppConfig update_configuration(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, manager_app_config=manager_app_config)

Update manager configuration

### Example


```python
from or_rest_client import AuthenticatedApiClient, ConfigurationApi
from or_rest_client.models.manager_app_config import ManagerAppConfig
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
api_instance = ConfigurationApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
manager_app_config = or_rest_client.ManagerAppConfig() # ManagerAppConfig |  (optional)

try:
    # Update manager configuration
    api_response = api_instance.update_configuration(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, manager_app_config=manager_app_config)
    print("The response of ConfigurationApi->update_configuration:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConfigurationApi->update_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **manager_app_config** | [**ManagerAppConfig**](ManagerAppConfig.md)|  | [optional] 

### Return type

[**ManagerAppConfig**](ManagerAppConfig.md)

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

