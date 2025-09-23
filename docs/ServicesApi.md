# or_rest_client.ServicesApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**deregister_service**](ServicesApi.md#deregister_service) | **DELETE** /service/{serviceId}/{instanceId} | Deregister an external service
[**get_global_services**](ServicesApi.md#get_global_services) | **GET** /service/global | List all registered external services that are globally accessible within the OpenRemote manager
[**get_service**](ServicesApi.md#get_service) | **GET** /service/{serviceId}/{instanceId} | Retrieve a specific external service by its serviceId and instanceId
[**get_services**](ServicesApi.md#get_services) | **GET** /service | List all registered external services for the given realm within the OpenRemote manager
[**heartbeat**](ServicesApi.md#heartbeat) | **PUT** /service/{serviceId}/{instanceId} | Update the active registration lease for the specified external service
[**register_global_service**](ServicesApi.md#register_global_service) | **POST** /service/global | Register a global external service with the OpenRemote manager
[**register_service**](ServicesApi.md#register_service) | **POST** /service | Register an external service with the OpenRemote manager


# **deregister_service**
> deregister_service(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Deregister an external service

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
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
api_instance = ServicesApi(client)
service_id = 'service_id_example' # str | 
instance_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Deregister an external service
    api_instance.deregister_service(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling ServicesApi->deregister_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **instance_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Service deregistered successfully |  -  |
**404** | Service instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_services**
> List[ExternalService] get_global_services(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

List all registered external services that are globally accessible within the OpenRemote manager

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
from or_rest_client.models.external_service import ExternalService
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
api_instance = ServicesApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # List all registered external services that are globally accessible within the OpenRemote manager
    api_response = api_instance.get_global_services(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ServicesApi->get_global_services:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServicesApi->get_global_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[ExternalService]**](ExternalService.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of registered external services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ExternalService get_service(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve a specific external service by its serviceId and instanceId

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
from or_rest_client.models.external_service import ExternalService
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
api_instance = ServicesApi(client)
service_id = 'service_id_example' # str | 
instance_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve a specific external service by its serviceId and instanceId
    api_response = api_instance.get_service(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ServicesApi->get_service:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServicesApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **instance_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**ExternalService**](ExternalService.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExternalService retrieved successfully |  -  |
**404** | ExternalService not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> List[ExternalService] get_services(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

List all registered external services for the given realm within the OpenRemote manager

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
from or_rest_client.models.external_service import ExternalService
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
api_instance = ServicesApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # List all registered external services for the given realm within the OpenRemote manager
    api_response = api_instance.get_services(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ServicesApi->get_services:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServicesApi->get_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[ExternalService]**](ExternalService.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of registered external services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heartbeat**
> heartbeat(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Update the active registration lease for the specified external service

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
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
api_instance = ServicesApi(client)
service_id = 'service_id_example' # str | 
instance_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Update the active registration lease for the specified external service
    api_instance.heartbeat(service_id, instance_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling ServicesApi->heartbeat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **instance_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Heartbeat sent successfully |  -  |
**404** | Service instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_global_service**
> ExternalService register_global_service(external_service, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Register a global external service with the OpenRemote manager

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
from or_rest_client.models.external_service import ExternalService
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
api_instance = ServicesApi(client)
external_service = or_rest_client.ExternalService() # ExternalService | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Register a global external service with the OpenRemote manager
    api_response = api_instance.register_global_service(external_service, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ServicesApi->register_global_service:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServicesApi->register_global_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_service** | [**ExternalService**](ExternalService.md)|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**ExternalService**](ExternalService.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service registered successfully |  -  |
**400** | Invalid external service object |  -  |
**409** | ExternalService instance already registered |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_service**
> ExternalService register_service(external_service, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Register an external service with the OpenRemote manager

### Example


```python
from or_rest_client import AuthenticatedApiClient, ServicesApi
from or_rest_client.models.external_service import ExternalService
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
api_instance = ServicesApi(client)
external_service = or_rest_client.ExternalService() # ExternalService | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Register an external service with the OpenRemote manager
    api_response = api_instance.register_service(external_service, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ServicesApi->register_service:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServicesApi->register_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_service** | [**ExternalService**](ExternalService.md)|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**ExternalService**](ExternalService.md)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service registered successfully |  -  |
**400** | Invalid external service object |  -  |
**409** | ExternalService instance already registered |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

