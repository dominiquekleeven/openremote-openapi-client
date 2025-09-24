# openremote_openapi_client.AlarmApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alarm**](AlarmApi.md#create_alarm) | **POST** /alarm | Create an alarm
[**get_alarm**](AlarmApi.md#get_alarm) | **GET** /alarm/{alarmId} | Retrieve an alarm
[**get_alarms**](AlarmApi.md#get_alarms) | **GET** /alarm | Retrieve all alarms or a subset using filter criteria
[**get_asset_links**](AlarmApi.md#get_asset_links) | **GET** /alarm/{alarmId}/assets | Retrieve the asset links of an alarm
[**remove_alarm**](AlarmApi.md#remove_alarm) | **DELETE** /alarm/{alarmId} | Remove an alarm
[**remove_alarms**](AlarmApi.md#remove_alarms) | **DELETE** /alarm | Remove alarms
[**set_asset_links**](AlarmApi.md#set_asset_links) | **PUT** /alarm/assets | Set the asset links of an alarm
[**update_alarm**](AlarmApi.md#update_alarm) | **PUT** /alarm/{alarmId} | Update an alarm


# **create_alarm**
> SentAlarm create_alarm(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)

Create an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/create-alarm)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
from openremote_openapi_client.models.sent_alarm import SentAlarm
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
api_instance = AlarmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_ids = ['asset_ids_example'] # List[str] |  (optional)

try:
    # Create an alarm
    api_response = api_instance.create_alarm(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_ids=asset_ids)
    print("The response of AlarmApi->create_alarm:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AlarmApi->create_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**SentAlarm**](SentAlarm.md)

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

# **get_alarm**
> SentAlarm get_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/get-alarm)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
from openremote_openapi_client.models.sent_alarm import SentAlarm
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
api_instance = AlarmApi(client)
alarm_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve an alarm
    api_response = api_instance.get_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of AlarmApi->get_alarm:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AlarmApi->get_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**SentAlarm**](SentAlarm.md)

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

# **get_alarms**
> List[SentAlarm] get_alarms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, status=status, asset_id=asset_id, assignee_id=assignee_id)

Retrieve all alarms or a subset using filter criteria

[View official API reference →](https://docs.openremote.io/docs/rest-api/get-alarms)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
from openremote_openapi_client.models.sent_alarm import SentAlarm
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
api_instance = AlarmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)
status = 'status_example' # str |  (optional)
asset_id = 'asset_id_example' # str |  (optional)
assignee_id = 'assignee_id_example' # str |  (optional)

try:
    # Retrieve all alarms or a subset using filter criteria
    api_response = api_instance.get_alarms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, status=status, asset_id=asset_id, assignee_id=assignee_id)
    print("The response of AlarmApi->get_alarms:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AlarmApi->get_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **assignee_id** | **str**|  | [optional] 

### Return type

[**List[SentAlarm]**](SentAlarm.md)

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

# **get_asset_links**
> List[AlarmAssetLink] get_asset_links(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)

Retrieve the asset links of an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/get-asset-links)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
from openremote_openapi_client.models.alarm_asset_link import AlarmAssetLink
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
api_instance = AlarmApi(client)
alarm_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)

try:
    # Retrieve the asset links of an alarm
    api_response = api_instance.get_asset_links(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)
    print("The response of AlarmApi->get_asset_links:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AlarmApi->get_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 

### Return type

[**List[AlarmAssetLink]**](AlarmAssetLink.md)

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

# **remove_alarm**
> remove_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Remove an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/remove-alarm)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
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
api_instance = AlarmApi(client)
alarm_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Remove an alarm
    api_instance.remove_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AlarmApi->remove_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **int**|  | 
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

# **remove_alarms**
> remove_alarms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Remove alarms

[View official API reference →](https://docs.openremote.io/docs/rest-api/remove-alarms)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
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
api_instance = AlarmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Remove alarms
    api_instance.remove_alarms(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AlarmApi->remove_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **set_asset_links**
> set_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Set the asset links of an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/set-asset-links)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
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
api_instance = AlarmApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Set the asset links of an alarm
    api_instance.set_asset_links(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AlarmApi->set_asset_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_alarm**
> update_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Update an alarm

[View official API reference →](https://docs.openremote.io/docs/rest-api/update-alarm)

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AlarmApi
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
api_instance = AlarmApi(client)
alarm_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Update an alarm
    api_instance.update_alarm(alarm_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling AlarmApi->update_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **int**|  | 
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

