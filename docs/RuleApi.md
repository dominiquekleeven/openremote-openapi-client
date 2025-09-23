# openremote_openapi_client.RuleApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_ruleset**](RuleApi.md#create_asset_ruleset) | **POST** /rules/asset | Create an asset ruleset
[**create_global_ruleset**](RuleApi.md#create_global_ruleset) | **POST** /rules | Create a global ruleset
[**create_realm_ruleset**](RuleApi.md#create_realm_ruleset) | **POST** /rules/realm | Create a realm ruleset
[**delete_asset_ruleset**](RuleApi.md#delete_asset_ruleset) | **DELETE** /rules/asset/{id} | Delete an asset ruleset
[**delete_global_ruleset**](RuleApi.md#delete_global_ruleset) | **DELETE** /rules/{id} | Delete a global ruleset
[**delete_realm_ruleset**](RuleApi.md#delete_realm_ruleset) | **DELETE** /rules/realm/{id} | Delete a realm ruleset
[**get_asset_engine_info**](RuleApi.md#get_asset_engine_info) | **GET** /rules/info/asset/{assetId} | Retrieve information about an asset rules engine
[**get_asset_geofences**](RuleApi.md#get_asset_geofences) | **GET** /rules/geofences/{assetId} | Get the geofences of an asset
[**get_asset_ruleset**](RuleApi.md#get_asset_ruleset) | **GET** /rules/asset/{id} | Retrieve an asset ruleset
[**get_asset_rulesets**](RuleApi.md#get_asset_rulesets) | **GET** /rules/asset/for/{assetId} | Retrieve the rules of an asset
[**get_global_engine_info**](RuleApi.md#get_global_engine_info) | **GET** /rules/info/global | Retrieve information about the global rules engine
[**get_global_ruleset**](RuleApi.md#get_global_ruleset) | **GET** /rules/{id} | Retrieve a global ruleset
[**get_global_rulesets**](RuleApi.md#get_global_rulesets) | **GET** /rules |  Retrieve the global rules
[**get_realm_engine_info**](RuleApi.md#get_realm_engine_info) | **GET** /rules/info/realm/{realm} | Retrieve information about a realm rules engine
[**get_realm_ruleset**](RuleApi.md#get_realm_ruleset) | **GET** /rules/realm/{id} | Retrieve a realm ruleset
[**get_realm_rulesets**](RuleApi.md#get_realm_rulesets) | **GET** /rules/realm/for/{realm} | Retrieve the rules of a realm
[**update_asset_ruleset**](RuleApi.md#update_asset_ruleset) | **PUT** /rules/asset/{id} | Update an asset ruleset
[**update_global_ruleset**](RuleApi.md#update_global_ruleset) | **PUT** /rules/{id} | Update a global ruleset
[**update_realm_ruleset**](RuleApi.md#update_realm_ruleset) | **PUT** /rules/realm/{id} | Update a realm ruleset


# **create_asset_ruleset**
> int create_asset_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ruleset=asset_ruleset)

Create an asset ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.asset_ruleset import AssetRuleset
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
api_instance = RuleApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_ruleset = openremote_openapi_client.AssetRuleset() # AssetRuleset |  (optional)

try:
    # Create an asset ruleset
    api_response = api_instance.create_asset_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ruleset=asset_ruleset)
    print("The response of RuleApi->create_asset_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->create_asset_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_ruleset** | [**AssetRuleset**](AssetRuleset.md)|  | [optional] 

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

# **create_global_ruleset**
> int create_global_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, global_ruleset=global_ruleset)

Create a global ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.global_ruleset import GlobalRuleset
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
api_instance = RuleApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
global_ruleset = openremote_openapi_client.GlobalRuleset() # GlobalRuleset |  (optional)

try:
    # Create a global ruleset
    api_response = api_instance.create_global_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, global_ruleset=global_ruleset)
    print("The response of RuleApi->create_global_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->create_global_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **global_ruleset** | [**GlobalRuleset**](GlobalRuleset.md)|  | [optional] 

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

# **create_realm_ruleset**
> int create_realm_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm_ruleset=realm_ruleset)

Create a realm ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.realm_ruleset import RealmRuleset
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
api_instance = RuleApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm_ruleset = openremote_openapi_client.RealmRuleset() # RealmRuleset |  (optional)

try:
    # Create a realm ruleset
    api_response = api_instance.create_realm_ruleset(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm_ruleset=realm_ruleset)
    print("The response of RuleApi->create_realm_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->create_realm_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm_ruleset** | [**RealmRuleset**](RealmRuleset.md)|  | [optional] 

### Return type

**int**

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

# **delete_asset_ruleset**
> delete_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete an asset ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete an asset ruleset
    api_instance.delete_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling RuleApi->delete_asset_ruleset: %s\n" % e)
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

# **delete_global_ruleset**
> delete_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a global ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a global ruleset
    api_instance.delete_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling RuleApi->delete_global_ruleset: %s\n" % e)
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
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_realm_ruleset**
> delete_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a realm ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a realm ruleset
    api_instance.delete_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling RuleApi->delete_realm_ruleset: %s\n" % e)
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
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_engine_info**
> RulesEngineInfo get_asset_engine_info(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve information about an asset rules engine

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.rules_engine_info import RulesEngineInfo
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
api_instance = RuleApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve information about an asset rules engine
    api_response = api_instance.get_asset_engine_info(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_asset_engine_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_asset_engine_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**RulesEngineInfo**](RulesEngineInfo.md)

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

# **get_asset_geofences**
> List[GeofenceDefinition] get_asset_geofences(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Get the geofences of an asset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.geofence_definition import GeofenceDefinition
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
api_instance = RuleApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Get the geofences of an asset
    api_response = api_instance.get_asset_geofences(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_asset_geofences:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_asset_geofences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[GeofenceDefinition]**](GeofenceDefinition.md)

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

# **get_asset_ruleset**
> AssetRuleset get_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve an asset ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.asset_ruleset import AssetRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve an asset ruleset
    api_response = api_instance.get_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_asset_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_asset_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**AssetRuleset**](AssetRuleset.md)

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

# **get_asset_rulesets**
> List[AssetRuleset] get_asset_rulesets(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)

Retrieve the rules of an asset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.asset_ruleset import AssetRuleset
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
api_instance = RuleApi(client)
asset_id = 'asset_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
language = ['language_example'] # List[str] |  (optional)
fully_populate = True # bool |  (optional)

try:
    # Retrieve the rules of an asset
    api_response = api_instance.get_asset_rulesets(asset_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)
    print("The response of RuleApi->get_asset_rulesets:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_asset_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **language** | [**List[str]**](str.md)|  | [optional] 
 **fully_populate** | **bool**|  | [optional] 

### Return type

[**List[AssetRuleset]**](AssetRuleset.md)

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

# **get_global_engine_info**
> RulesEngineInfo get_global_engine_info(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve information about the global rules engine

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.rules_engine_info import RulesEngineInfo
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
api_instance = RuleApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve information about the global rules engine
    api_response = api_instance.get_global_engine_info(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_global_engine_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_global_engine_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**RulesEngineInfo**](RulesEngineInfo.md)

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

# **get_global_ruleset**
> GlobalRuleset get_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve a global ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.global_ruleset import GlobalRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve a global ruleset
    api_response = api_instance.get_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_global_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_global_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**GlobalRuleset**](GlobalRuleset.md)

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

# **get_global_rulesets**
> List[GlobalRuleset] get_global_rulesets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)

 Retrieve the global rules

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.global_ruleset import GlobalRuleset
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
api_instance = RuleApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
language = ['language_example'] # List[str] |  (optional)
fully_populate = True # bool |  (optional)

try:
    #  Retrieve the global rules
    api_response = api_instance.get_global_rulesets(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)
    print("The response of RuleApi->get_global_rulesets:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_global_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **language** | [**List[str]**](str.md)|  | [optional] 
 **fully_populate** | **bool**|  | [optional] 

### Return type

[**List[GlobalRuleset]**](GlobalRuleset.md)

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

# **get_realm_engine_info**
> RulesEngineInfo get_realm_engine_info(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve information about a realm rules engine

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.rules_engine_info import RulesEngineInfo
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
api_instance = RuleApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve information about a realm rules engine
    api_response = api_instance.get_realm_engine_info(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_realm_engine_info:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_realm_engine_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**RulesEngineInfo**](RulesEngineInfo.md)

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

# **get_realm_ruleset**
> RealmRuleset get_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve a realm ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.realm_ruleset import RealmRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve a realm ruleset
    api_response = api_instance.get_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of RuleApi->get_realm_ruleset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_realm_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**RealmRuleset**](RealmRuleset.md)

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

# **get_realm_rulesets**
> List[RealmRuleset] get_realm_rulesets(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)

Retrieve the rules of a realm

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.realm_ruleset import RealmRuleset
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
api_instance = RuleApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
language = ['language_example'] # List[str] |  (optional)
fully_populate = True # bool |  (optional)

try:
    # Retrieve the rules of a realm
    api_response = api_instance.get_realm_rulesets(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, language=language, fully_populate=fully_populate)
    print("The response of RuleApi->get_realm_rulesets:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RuleApi->get_realm_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **language** | [**List[str]**](str.md)|  | [optional] 
 **fully_populate** | **bool**|  | [optional] 

### Return type

[**List[RealmRuleset]**](RealmRuleset.md)

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

# **update_asset_ruleset**
> update_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ruleset=asset_ruleset)

Update an asset ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.asset_ruleset import AssetRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_ruleset = openremote_openapi_client.AssetRuleset() # AssetRuleset |  (optional)

try:
    # Update an asset ruleset
    api_instance.update_asset_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ruleset=asset_ruleset)
except Exception as e:
    print("Exception when calling RuleApi->update_asset_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_ruleset** | [**AssetRuleset**](AssetRuleset.md)|  | [optional] 

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

# **update_global_ruleset**
> update_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, global_ruleset=global_ruleset)

Update a global ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.global_ruleset import GlobalRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
global_ruleset = openremote_openapi_client.GlobalRuleset() # GlobalRuleset |  (optional)

try:
    # Update a global ruleset
    api_instance.update_global_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, global_ruleset=global_ruleset)
except Exception as e:
    print("Exception when calling RuleApi->update_global_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **global_ruleset** | [**GlobalRuleset**](GlobalRuleset.md)|  | [optional] 

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

# **update_realm_ruleset**
> update_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm_ruleset=realm_ruleset)

Update a realm ruleset

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, RuleApi
from openremote_openapi_client.models.realm_ruleset import RealmRuleset
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
api_instance = RuleApi(client)
id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm_ruleset = openremote_openapi_client.RealmRuleset() # RealmRuleset |  (optional)

try:
    # Update a realm ruleset
    api_instance.update_realm_ruleset(id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm_ruleset=realm_ruleset)
except Exception as e:
    print("Exception when calling RuleApi->update_realm_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm_ruleset** | [**RealmRuleset**](RealmRuleset.md)|  | [optional] 

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

