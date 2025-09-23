# openremote_openapi_client.AssetDatapointApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datapoint_export**](AssetDatapointApi.md#get_datapoint_export) | **GET** /asset/datapoint/export | Retrieve a datapoint export of an asset attribute
[**get_datapoint_period**](AssetDatapointApi.md#get_datapoint_period) | **GET** /asset/datapoint/periods | Retrieve a datapoint period of an asset attribute
[**get_datapoints**](AssetDatapointApi.md#get_datapoints) | **POST** /asset/datapoint/{assetId}/{attributeName} | Retrieve the historical datapoints of an asset attribute


# **get_datapoint_export**
> get_datapoint_export(attribute_refs=attribute_refs, from_timestamp=from_timestamp, to_timestamp=to_timestamp)

Retrieve a datapoint export of an asset attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetDatapointApi
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
api_instance = AssetDatapointApi(client)
attribute_refs = 'attribute_refs_example' # str |  (optional)
from_timestamp = 56 # int |  (optional)
to_timestamp = 56 # int |  (optional)

try:
    # Retrieve a datapoint export of an asset attribute
    api_instance.get_datapoint_export(attribute_refs=attribute_refs, from_timestamp=from_timestamp, to_timestamp=to_timestamp)
except Exception as e:
    print("Exception when calling AssetDatapointApi->get_datapoint_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_refs** | **str**|  | [optional] 
 **from_timestamp** | **int**|  | [optional] 
 **to_timestamp** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openid](../README.md#openid), [openid](../README.md#openid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datapoint_period**
> DatapointPeriod get_datapoint_period(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_id=asset_id, attribute_name=attribute_name)

Retrieve a datapoint period of an asset attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetDatapointApi
from openremote_openapi_client.models.datapoint_period import DatapointPeriod
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
api_instance = AssetDatapointApi(client)
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_id = 'asset_id_example' # str |  (optional)
attribute_name = 'attribute_name_example' # str |  (optional)

try:
    # Retrieve a datapoint period of an asset attribute
    api_response = api_instance.get_datapoint_period(authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_id=asset_id, attribute_name=attribute_name)
    print("The response of AssetDatapointApi->get_datapoint_period:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetDatapointApi->get_datapoint_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **attribute_name** | **str**|  | [optional] 

### Return type

[**DatapointPeriod**](DatapointPeriod.md)

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

# **get_datapoints**
> List[ValueDatapointObject] get_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_datapoint_query=asset_datapoint_query)

Retrieve the historical datapoints of an asset attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetDatapointApi
from openremote_openapi_client.models.asset_datapoint_query import AssetDatapointQuery
from openremote_openapi_client.models.value_datapoint_object import ValueDatapointObject
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
api_instance = AssetDatapointApi(client)
asset_id = 'asset_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_datapoint_query = openremote_openapi_client.AssetDatapointQuery() # AssetDatapointQuery |  (optional)

try:
    # Retrieve the historical datapoints of an asset attribute
    api_response = api_instance.get_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_datapoint_query=asset_datapoint_query)
    print("The response of AssetDatapointApi->get_datapoints:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetDatapointApi->get_datapoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **asset_datapoint_query** | [**AssetDatapointQuery**](AssetDatapointQuery.md)|  | [optional] 

### Return type

[**List[ValueDatapointObject]**](ValueDatapointObject.md)

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

