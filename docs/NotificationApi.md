# openremote_openapi_client.NotificationApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationApi.md#get_notifications) | **GET** /notification | Retrieve all sent notifications by targets
[**notification_acknowledged**](NotificationApi.md#notification_acknowledged) | **PUT** /notification/{notificationId}/acknowledged | Update a notification as acknowledged
[**notification_delivered**](NotificationApi.md#notification_delivered) | **PUT** /notification/{notificationId}/delivered | Update a notification as delivered
[**remove_notification**](NotificationApi.md#remove_notification) | **DELETE** /notification/{notificationId} | Delete a sent notification
[**remove_notifications**](NotificationApi.md#remove_notifications) | **DELETE** /notification | Delete all sent notifications by targets
[**send_notification**](NotificationApi.md#send_notification) | **POST** /notification/alert | Send a notification to one or more targets


# **get_notifications**
> List[SentNotification] get_notifications(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, id=id, type=type, var_from=var_from, to=to, realm_id=realm_id, user_id=user_id, asset_id=asset_id)

Retrieve all sent notifications by targets

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
from openremote_openapi_client.models.sent_notification import SentNotification
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
api_instance = NotificationApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
id = 56 # int |  (optional)
type = 'type_example' # str |  (optional)
var_from = 56 # int |  (optional)
to = 56 # int |  (optional)
realm_id = 'realm_id_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
asset_id = 'asset_id_example' # str |  (optional)

try:
    # Retrieve all sent notifications by targets
    api_response = api_instance.get_notifications(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, id=id, type=type, var_from=var_from, to=to, realm_id=realm_id, user_id=user_id, asset_id=asset_id)
    print("The response of NotificationApi->get_notifications:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **type** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **realm_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 

### Return type

[**List[SentNotification]**](SentNotification.md)

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

# **notification_acknowledged**
> notification_acknowledged(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, target_id=target_id, body=body)

Update a notification as acknowledged

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
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
api_instance = NotificationApi(client)
notification_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
target_id = 'target_id_example' # str |  (optional)
body = None # object |  (optional)

try:
    # Update a notification as acknowledged
    api_instance.notification_acknowledged(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, target_id=target_id, body=body)
except Exception as e:
    print("Exception when calling NotificationApi->notification_acknowledged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **target_id** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

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

# **notification_delivered**
> notification_delivered(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, target_id=target_id)

Update a notification as delivered

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
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
api_instance = NotificationApi(client)
notification_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
target_id = 'target_id_example' # str |  (optional)

try:
    # Update a notification as delivered
    api_instance.notification_delivered(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, target_id=target_id)
except Exception as e:
    print("Exception when calling NotificationApi->notification_delivered: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **target_id** | **str**|  | [optional] 

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

# **remove_notification**
> remove_notification(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a sent notification

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
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
api_instance = NotificationApi(client)
notification_id = 56 # int | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a sent notification
    api_instance.remove_notification(notification_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling NotificationApi->remove_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**|  | 
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

# **remove_notifications**
> remove_notifications(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, id=id, type=type, var_from=var_from, to=to, realm_id=realm_id, user_id=user_id, asset_id=asset_id)

Delete all sent notifications by targets

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
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
api_instance = NotificationApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
id = 56 # int |  (optional)
type = 'type_example' # str |  (optional)
var_from = 56 # int |  (optional)
to = 56 # int |  (optional)
realm_id = 'realm_id_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
asset_id = 'asset_id_example' # str |  (optional)

try:
    # Delete all sent notifications by targets
    api_instance.remove_notifications(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, id=id, type=type, var_from=var_from, to=to, realm_id=realm_id, user_id=user_id, asset_id=asset_id)
except Exception as e:
    print("Exception when calling NotificationApi->remove_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **type** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **realm_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 

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

# **send_notification**
> send_notification(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, notification=notification)

Send a notification to one or more targets

### Example


```python
from openremote_openapi_client import AuthenticatedApiClient, NotificationApi
from openremote_openapi_client.models.notification import Notification
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
api_instance = NotificationApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
notification = openremote_openapi_client.Notification() # Notification |  (optional)

try:
    # Send a notification to one or more targets
    api_instance.send_notification(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, notification=notification)
except Exception as e:
    print("Exception when calling NotificationApi->send_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **notification** | [**Notification**](Notification.md)|  | [optional] 

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

