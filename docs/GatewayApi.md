# or_rest_client.GatewayApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection**](GatewayApi.md#delete_connection) | **DELETE** /gateway/connection/{realm} | Delete the gateway connection of a realm
[**delete_connections**](GatewayApi.md#delete_connections) | **DELETE** /gateway/connection | Delete the gateway connections of multiple realms
[**get_active_tunnel_info**](GatewayApi.md#get_active_tunnel_info) | **GET** /gateway/tunnel/{realm}/{id}/{target}/{targetPort} | Retrieve the gateway tunnel information of tunnel for a gateway in a realm
[**get_all_active_tunnel_infos**](GatewayApi.md#get_all_active_tunnel_infos) | **GET** /gateway/tunnel/{realm} | Retrieve all active gateway tunnel information of a realm
[**get_connection**](GatewayApi.md#get_connection) | **GET** /gateway/connection/{realm} | Retrieve the gateway connection of a realm
[**get_connection_status**](GatewayApi.md#get_connection_status) | **GET** /gateway/status/{realm} | Retrieve the gateway connection status of a realm
[**get_connections**](GatewayApi.md#get_connections) | **GET** /gateway/connection | Retrieve the gateway connections of all realms
[**get_gateway_active_tunnel_infos**](GatewayApi.md#get_gateway_active_tunnel_infos) | **GET** /gateway/tunnel/{realm}/{id} | Retrieve the active gateway tunnel information of gateway in a realm
[**set_connection**](GatewayApi.md#set_connection) | **PUT** /gateway/connection/{realm} | Update the gateway connection of a realm
[**start_tunnel**](GatewayApi.md#start_tunnel) | **POST** /gateway/tunnel | Start a tunnel for a gateway
[**stop_tunnel**](GatewayApi.md#stop_tunnel) | **DELETE** /gateway/tunnel | Stop a tunnel for a gateway


# **delete_connection**
> delete_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete the gateway connection of a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete the gateway connection of a realm
    api_instance.delete_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling GatewayApi->delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
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

# **delete_connections**
> delete_connections(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)

Delete the gateway connections of multiple realms

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
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
api_instance = GatewayApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = ['realm_example'] # List[str] |  (optional)

try:
    # Delete the gateway connections of multiple realms
    api_instance.delete_connections(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)
except Exception as e:
    print("Exception when calling GatewayApi->delete_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | [**List[str]**](str.md)|  | [optional] 

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

# **get_active_tunnel_info**
> GatewayTunnelInfo get_active_tunnel_info(realm, id, target, target_port, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the gateway tunnel information of tunnel for a gateway in a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_tunnel_info import GatewayTunnelInfo
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
id = 'id_example' # str | 
target = 'target_example' # str | 
target_port = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the gateway tunnel information of tunnel for a gateway in a realm
    api_response = api_instance.get_active_tunnel_info(realm, id, target, target_port, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_active_tunnel_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_active_tunnel_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **id** | **str**|  | 
 **target** | **str**|  | 
 **target_port** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**GatewayTunnelInfo**](GatewayTunnelInfo.md)

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

# **get_all_active_tunnel_infos**
> List[GatewayTunnelInfo] get_all_active_tunnel_infos(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve all active gateway tunnel information of a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_tunnel_info import GatewayTunnelInfo
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve all active gateway tunnel information of a realm
    api_response = api_instance.get_all_active_tunnel_infos(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_all_active_tunnel_infos:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_all_active_tunnel_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[GatewayTunnelInfo]**](GatewayTunnelInfo.md)

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

# **get_connection**
> GatewayConnection get_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the gateway connection of a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_connection import GatewayConnection
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the gateway connection of a realm
    api_response = api_instance.get_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_connection:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**GatewayConnection**](GatewayConnection.md)

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

# **get_connection_status**
> str get_connection_status(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the gateway connection status of a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the gateway connection status of a realm
    api_response = api_instance.get_connection_status(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_connection_status:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

**str**

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

# **get_connections**
> List[GatewayConnection] get_connections(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the gateway connections of all realms

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_connection import GatewayConnection
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
api_instance = GatewayApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the gateway connections of all realms
    api_response = api_instance.get_connections(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_connections:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[GatewayConnection]**](GatewayConnection.md)

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

# **get_gateway_active_tunnel_infos**
> List[GatewayTunnelInfo] get_gateway_active_tunnel_infos(realm, id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the active gateway tunnel information of gateway in a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_tunnel_info import GatewayTunnelInfo
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
id = 'id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the active gateway tunnel information of gateway in a realm
    api_response = api_instance.get_gateway_active_tunnel_infos(realm, id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of GatewayApi->get_gateway_active_tunnel_infos:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->get_gateway_active_tunnel_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[GatewayTunnelInfo]**](GatewayTunnelInfo.md)

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

# **set_connection**
> set_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, gateway_connection=gateway_connection)

Update the gateway connection of a realm

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_connection import GatewayConnection
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
api_instance = GatewayApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
gateway_connection = or_rest_client.GatewayConnection() # GatewayConnection |  (optional)

try:
    # Update the gateway connection of a realm
    api_instance.set_connection(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, gateway_connection=gateway_connection)
except Exception as e:
    print("Exception when calling GatewayApi->set_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **gateway_connection** | [**GatewayConnection**](GatewayConnection.md)|  | [optional] 

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

# **start_tunnel**
> GatewayTunnelInfo start_tunnel(gateway_tunnel_info=gateway_tunnel_info)

Start a tunnel for a gateway

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_tunnel_info import GatewayTunnelInfo
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
api_instance = GatewayApi(client)
gateway_tunnel_info = or_rest_client.GatewayTunnelInfo() # GatewayTunnelInfo |  (optional)

try:
    # Start a tunnel for a gateway
    api_response = api_instance.start_tunnel(gateway_tunnel_info=gateway_tunnel_info)
    print("The response of GatewayApi->start_tunnel:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GatewayApi->start_tunnel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_tunnel_info** | [**GatewayTunnelInfo**](GatewayTunnelInfo.md)|  | [optional] 

### Return type

[**GatewayTunnelInfo**](GatewayTunnelInfo.md)

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

# **stop_tunnel**
> stop_tunnel(gateway_tunnel_info=gateway_tunnel_info)

Stop a tunnel for a gateway

### Example


```python
from or_rest_client import AuthenticatedApiClient, GatewayApi
from or_rest_client.models.gateway_tunnel_info import GatewayTunnelInfo
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
api_instance = GatewayApi(client)
gateway_tunnel_info = or_rest_client.GatewayTunnelInfo() # GatewayTunnelInfo |  (optional)

try:
    # Stop a tunnel for a gateway
    api_instance.stop_tunnel(gateway_tunnel_info=gateway_tunnel_info)
except Exception as e:
    print("Exception when calling GatewayApi->stop_tunnel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_tunnel_info** | [**GatewayTunnelInfo**](GatewayTunnelInfo.md)|  | [optional] 

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

