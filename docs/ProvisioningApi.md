# openremote_openapi_client.ProvisioningApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_config**](ProvisioningApi.md#create_provisioning_config) | **POST** /provisioning | Create a provisioning configuration
[**delete_provisioning_config**](ProvisioningApi.md#delete_provisioning_config) | **DELETE** /provisioning/{id} | Delete a provisioning configuration
[**get_provisioning_configs**](ProvisioningApi.md#get_provisioning_configs) | **GET** /provisioning | Retrieve all provisioning configurations
[**update_provisioning_config**](ProvisioningApi.md#update_provisioning_config) | **PUT** /provisioning/{id} | Update a provisioning configuration


# **create_provisioning_config**
> int create_provisioning_config(provisioning_config_object_object=provisioning_config_object_object)

Create a provisioning configuration

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, ProvisioningApi
from openremote_openapi_client.models.provisioning_config_object_object import ProvisioningConfigObjectObject
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
api_instance = ProvisioningApi(client)
provisioning_config_object_object = openremote_openapi_client.ProvisioningConfigObjectObject() # ProvisioningConfigObjectObject |  (optional)

try:
    # Create a provisioning configuration
    api_response = api_instance.create_provisioning_config(provisioning_config_object_object=provisioning_config_object_object)
    print("The response of ProvisioningApi->create_provisioning_config:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvisioningApi->create_provisioning_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_config_object_object** | [**ProvisioningConfigObjectObject**](ProvisioningConfigObjectObject.md)|  | [optional] 

### Return type

**int**

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

# **delete_provisioning_config**
> delete_provisioning_config(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a provisioning configuration

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, ProvisioningApi
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
api_instance = ProvisioningApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a provisioning configuration
    api_instance.delete_provisioning_config(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling ProvisioningApi->delete_provisioning_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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

# **get_provisioning_configs**
> List[ProvisioningConfigObjectObject] get_provisioning_configs()

Retrieve all provisioning configurations

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, ProvisioningApi
from openremote_openapi_client.models.provisioning_config_object_object import ProvisioningConfigObjectObject
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
api_instance = ProvisioningApi(client)

try:
    # Retrieve all provisioning configurations
    api_response = api_instance.get_provisioning_configs()
    print("The response of ProvisioningApi->get_provisioning_configs:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvisioningApi->get_provisioning_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProvisioningConfigObjectObject]**](ProvisioningConfigObjectObject.md)

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

# **update_provisioning_config**
> update_provisioning_config(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, provisioning_config_object_object=provisioning_config_object_object)

Update a provisioning configuration

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, ProvisioningApi
from openremote_openapi_client.models.provisioning_config_object_object import ProvisioningConfigObjectObject
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
api_instance = ProvisioningApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
provisioning_config_object_object = openremote_openapi_client.ProvisioningConfigObjectObject() # ProvisioningConfigObjectObject |  (optional)

try:
    # Update a provisioning configuration
    api_instance.update_provisioning_config(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, provisioning_config_object_object=provisioning_config_object_object)
except Exception as e:
    print("Exception when calling ProvisioningApi->update_provisioning_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **provisioning_config_object_object** | [**ProvisioningConfigObjectObject**](ProvisioningConfigObjectObject.md)|  | [optional] 

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

