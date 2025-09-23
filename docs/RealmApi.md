# openremote_openapi_client.RealmApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_realm**](RealmApi.md#create_realm) | **POST** /realm | Create a new realm
[**delete_realm**](RealmApi.md#delete_realm) | **DELETE** /realm/{name} | Delete a realm
[**get_accessible_realms**](RealmApi.md#get_accessible_realms) | **GET** /realm/accessible | Retrieve accessible realms for the authenticated user
[**get_all_realms**](RealmApi.md#get_all_realms) | **GET** /realm | Retrieve all realms
[**get_realm**](RealmApi.md#get_realm) | **GET** /realm/{name} | Retrieve details about the currently authenticated and active realm
[**update_realm**](RealmApi.md#update_realm) | **PUT** /realm/{name} | Update a realm


# **create_realm**
> create_realm(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)

Create a new realm

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
from openremote_openapi_client.models.realm import Realm
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
api_instance = RealmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = openremote_openapi_client.Realm() # Realm |  (optional)

try:
    # Create a new realm
    api_instance.create_realm(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)
except Exception as e:
    print("Exception when calling RealmApi->create_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | [**Realm**](Realm.md)|  | [optional] 

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

# **delete_realm**
> delete_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a realm

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
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
api_instance = RealmApi(client)
name = 'name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a realm
    api_instance.delete_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling RealmApi->delete_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
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

# **get_accessible_realms**
> List[Realm] get_accessible_realms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve accessible realms for the authenticated user

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
from openremote_openapi_client.models.realm import Realm
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
api_instance = RealmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve accessible realms for the authenticated user
    api_response = api_instance.get_accessible_realms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RealmApi->get_accessible_realms:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RealmApi->get_accessible_realms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[Realm]**](Realm.md)

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

# **get_all_realms**
> List[Realm] get_all_realms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve all realms

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
from openremote_openapi_client.models.realm import Realm
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
api_instance = RealmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve all realms
    api_response = api_instance.get_all_realms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RealmApi->get_all_realms:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RealmApi->get_all_realms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[Realm]**](Realm.md)

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

# **get_realm**
> Realm get_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve details about the currently authenticated and active realm

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
from openremote_openapi_client.models.realm import Realm
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
api_instance = RealmApi(client)
name = 'name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve details about the currently authenticated and active realm
    api_response = api_instance.get_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RealmApi->get_realm:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RealmApi->get_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**Realm**](Realm.md)

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

# **update_realm**
> update_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)

Update a realm

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RealmApi
from openremote_openapi_client.models.realm import Realm
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
api_instance = RealmApi(client)
name = 'name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = openremote_openapi_client.Realm() # Realm |  (optional)

try:
    # Update a realm
    api_instance.update_realm(name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)
except Exception as e:
    print("Exception when calling RealmApi->update_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | [**Realm**](Realm.md)|  | [optional] 

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

