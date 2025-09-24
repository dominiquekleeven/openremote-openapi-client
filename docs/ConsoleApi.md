# openremote_openapi_client.ConsoleApi

**[Official OpenRemote REST API Docs](https://docs.openremote.io/docs/category/rest-api)**

Method | HTTP request | Description
------------- | ------------- | -------------
[**register**](ConsoleApi.md#register) | **POST** /console/register | Create or update the registration for a console


# **register**
> ConsoleRegistration register(console_registration, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Create or update the registration for a console

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, ConsoleApi
from openremote_openapi_client.models.console_registration import ConsoleRegistration
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
api_instance = ConsoleApi(client)
console_registration = ConsoleRegistration() # ConsoleRegistration | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Create or update the registration for a console
    api_response = api_instance.register(console_registration, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of ConsoleApi->register:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConsoleApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **console_registration** | [**ConsoleRegistration**](ConsoleRegistration.md)|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**ConsoleRegistration**](ConsoleRegistration.md)

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

