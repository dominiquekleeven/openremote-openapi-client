# openremote_openapi_client.AssetPredictedDatapointApi

**[Official OpenRemote REST API Docs](https://docs.openremote.io/docs/category/rest-api)**

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_predicted_datapoints**](AssetPredictedDatapointApi.md#get_predicted_datapoints) | **POST** /asset/predicted/{assetId}/{attributeName} | Retrieve the predicted datapoints of an asset attribute
[**write_predicted_datapoints**](AssetPredictedDatapointApi.md#write_predicted_datapoints) | **PUT** /asset/predicted/{assetId}/{attributeName} | Write the predicted datapoints of an asset attribute


# **get_predicted_datapoints**
> List[ValueDatapointObject] get_predicted_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_datapoint_query=asset_datapoint_query)

Retrieve the predicted datapoints of an asset attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetPredictedDatapointApi
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
api_instance = AssetPredictedDatapointApi(client)
asset_id = 'asset_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
asset_datapoint_query = AssetDatapointQuery() # AssetDatapointQuery |  (optional)

try:
    # Retrieve the predicted datapoints of an asset attribute
    api_response = api_instance.get_predicted_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, asset_datapoint_query=asset_datapoint_query)
    print("The response of AssetPredictedDatapointApi->get_predicted_datapoints:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AssetPredictedDatapointApi->get_predicted_datapoints: %s\n" % e)
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

# **write_predicted_datapoints**
> write_predicted_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, value_datapoint_object=value_datapoint_object)

Write the predicted datapoints of an asset attribute

### Example


```python
from openremote_openapi_client import OpenRemoteApiClient, AssetPredictedDatapointApi
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
api_instance = AssetPredictedDatapointApi(client)
asset_id = 'asset_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
value_datapoint_object = [openremote_openapi_client.ValueDatapointObject()] # List[ValueDatapointObject] |  (optional)

try:
    # Write the predicted datapoints of an asset attribute
    api_instance.write_predicted_datapoints(asset_id, attribute_name, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, value_datapoint_object=value_datapoint_object)
except Exception as e:
    print("Exception when calling AssetPredictedDatapointApi->write_predicted_datapoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **value_datapoint_object** | [**List[ValueDatapointObject]**](ValueDatapointObject.md)|  | [optional] 

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

