# openremote_openapi_client.SyslogApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_events**](SyslogApi.md#clear_events) | **DELETE** /syslog/event | Clear the syslog events
[**get_config**](SyslogApi.md#get_config) | **GET** /syslog/config | Retrieve the syslog configuration
[**get_events**](SyslogApi.md#get_events) | **GET** /syslog/event | Retrieve the syslog events
[**update_config**](SyslogApi.md#update_config) | **PUT** /syslog/config | Update the syslog configuration


# **clear_events**
> clear_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Clear the syslog events

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, SyslogApi
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
api_instance = SyslogApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Clear the syslog events
    api_instance.clear_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling SyslogApi->clear_events: %s\n" % e)
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

# **get_config**
> SyslogConfig get_config(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve the syslog configuration

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, SyslogApi
from openremote_openapi_client.models.syslog_config import SyslogConfig
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
api_instance = SyslogApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve the syslog configuration
    api_response = api_instance.get_config(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of SyslogApi->get_config:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SyslogApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**SyslogConfig**](SyslogConfig.md)

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

# **get_events**
> get_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, level=level, per_page=per_page, page=page, var_from=var_from, to=to, category=category, sub_category=sub_category)

Retrieve the syslog events

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, SyslogApi
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
api_instance = SyslogApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
level = 'level_example' # str |  (optional)
per_page = 56 # int |  (optional)
page = 56 # int |  (optional)
var_from = 56 # int |  (optional)
to = 56 # int |  (optional)
category = ['category_example'] # List[str] |  (optional)
sub_category = ['sub_category_example'] # List[str] |  (optional)

try:
    # Retrieve the syslog events
    api_instance.get_events(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, level=level, per_page=per_page, page=page, var_from=var_from, to=to, category=category, sub_category=sub_category)
except Exception as e:
    print("Exception when calling SyslogApi->get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **level** | **str**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **category** | [**List[str]**](str.md)|  | [optional] 
 **sub_category** | [**List[str]**](str.md)|  | [optional] 

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

# **update_config**
> update_config(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, syslog_config=syslog_config)

Update the syslog configuration

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, SyslogApi
from openremote_openapi_client.models.syslog_config import SyslogConfig
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
api_instance = SyslogApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
syslog_config = openremote_openapi_client.SyslogConfig() # SyslogConfig |  (optional)

try:
    # Update the syslog configuration
    api_instance.update_config(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, syslog_config=syslog_config)
except Exception as e:
    print("Exception when calling SyslogApi->update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **syslog_config** | [**SyslogConfig**](SyslogConfig.md)|  | [optional] 

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

