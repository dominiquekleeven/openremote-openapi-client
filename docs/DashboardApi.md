# or_rest_client.DashboardApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /dashboard | Create a dashboard
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /dashboard/{realm}/{dashboardId} | Delete a dashboard
[**get_all_realm_dashboards**](DashboardApi.md#get_all_realm_dashboards) | **GET** /dashboard/all/{realm} | Retrieve all accessible dashboards
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /dashboard/{realm}/{dashboardId} | Retrieve a dashboard
[**query_dashboards**](DashboardApi.md#query_dashboards) | **POST** /dashboard/query | Retrieve dashboards using a query
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PUT** /dashboard | Update a dashboard


# **create_dashboard**
> Dashboard create_dashboard(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard=dashboard)

Create a dashboard

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
from or_rest_client.models.dashboard import Dashboard
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
api_instance = DashboardApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
dashboard = or_rest_client.Dashboard() # Dashboard |  (optional)

try:
    # Create a dashboard
    api_response = api_instance.create_dashboard(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard=dashboard)
    print("The response of DashboardApi->create_dashboard:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **dashboard** | [**Dashboard**](Dashboard.md)|  | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

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

# **delete_dashboard**
> delete_dashboard(realm, dashboard_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Delete a dashboard

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
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
api_instance = DashboardApi(client)
realm = 'realm_example' # str | 
dashboard_id = 'dashboard_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Delete a dashboard
    api_instance.delete_dashboard(realm, dashboard_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
except Exception as e:
    print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **dashboard_id** | **str**|  | 
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

# **get_all_realm_dashboards**
> List[Dashboard] get_all_realm_dashboards(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve all accessible dashboards

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
from or_rest_client.models.dashboard import Dashboard
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
api_instance = DashboardApi(client)
realm = 'realm_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve all accessible dashboards
    api_response = api_instance.get_all_realm_dashboards(realm, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of DashboardApi->get_all_realm_dashboards:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DashboardApi->get_all_realm_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**List[Dashboard]**](Dashboard.md)

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

# **get_dashboard**
> Dashboard get_dashboard(realm, dashboard_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)

Retrieve a dashboard

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
from or_rest_client.models.dashboard import Dashboard
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
api_instance = DashboardApi(client)
realm = 'realm_example' # str | 
dashboard_id = 'dashboard_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)

try:
    # Retrieve a dashboard
    api_response = api_instance.get_dashboard(realm, dashboard_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host)
    print("The response of DashboardApi->get_dashboard:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  | 
 **dashboard_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

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

# **query_dashboards**
> List[Dashboard] query_dashboards(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard_query=dashboard_query)

Retrieve dashboards using a query

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
from or_rest_client.models.dashboard import Dashboard
from or_rest_client.models.dashboard_query import DashboardQuery
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
api_instance = DashboardApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
dashboard_query = or_rest_client.DashboardQuery() # DashboardQuery |  (optional)

try:
    # Retrieve dashboards using a query
    api_response = api_instance.query_dashboards(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard_query=dashboard_query)
    print("The response of DashboardApi->query_dashboards:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DashboardApi->query_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **dashboard_query** | [**DashboardQuery**](DashboardQuery.md)|  | [optional] 

### Return type

[**List[Dashboard]**](Dashboard.md)

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

# **update_dashboard**
> Dashboard update_dashboard(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard=dashboard)

Update a dashboard

### Example


```python
from or_rest_client import AuthenticatedApiClient, DashboardApi
from or_rest_client.models.dashboard import Dashboard
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
api_instance = DashboardApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
dashboard = or_rest_client.Dashboard() # Dashboard |  (optional)

try:
    # Update a dashboard
    api_response = api_instance.update_dashboard(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, dashboard=dashboard)
    print("The response of DashboardApi->update_dashboard:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **dashboard** | [**Dashboard**](Dashboard.md)|  | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

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

