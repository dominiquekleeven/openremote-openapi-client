# or_rest_client.StatusApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_status**](StatusApi.md#get_health_status) | **GET** /health | Retrieve the health status of the system
[**get_info**](StatusApi.md#get_info) | **GET** /info | Retrieve the system information


# **get_health_status**
> Dict[str, object] get_health_status()

Retrieve the health status of the system

### Example


```python
from or_rest_client import AuthenticatedApiClient, StatusApi
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
api_instance = StatusApi(client)

try:
    # Retrieve the health status of the system
    api_response = api_instance.get_health_status()
    print("The response of StatusApi->get_health_status:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling StatusApi->get_health_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

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

# **get_info**
> Dict[str, object] get_info()

Retrieve the system information

### Example


```python
from or_rest_client import AuthenticatedApiClient, StatusApi
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
api_instance = StatusApi(client)

try:
    # Retrieve the system information
    api_response = api_instance.get_info()
    print("The response of StatusApi->get_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling StatusApi->get_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

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

