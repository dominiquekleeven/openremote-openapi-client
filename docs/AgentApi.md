# or_rest_client.AgentApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_protocol_asset_discovery**](AgentApi.md#do_protocol_asset_discovery) | **GET** /agent/assetDiscovery/{agentId} | Do protocol asset discovery
[**do_protocol_asset_import**](AgentApi.md#do_protocol_asset_import) | **POST** /agent/assetImport/{agentId} | Do protocol asset import
[**do_protocol_instance_discovery**](AgentApi.md#do_protocol_instance_discovery) | **GET** /agent/instanceDiscovery/{agentType} | Do protocol instance discovery


# **do_protocol_asset_discovery**
> List[AssetTreeNode] do_protocol_asset_discovery(agent_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)

Do protocol asset discovery

### Example


```python
from or_rest_client import AuthenticatedApiClient, AgentApi
from or_rest_client.models.asset_tree_node import AssetTreeNode
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
api_instance = AgentApi(client)
agent_id = 'agent_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)

try:
    # Do protocol asset discovery
    api_response = api_instance.do_protocol_asset_discovery(agent_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm)
    print("The response of AgentApi->do_protocol_asset_discovery:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AgentApi->do_protocol_asset_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 

### Return type

[**List[AssetTreeNode]**](AssetTreeNode.md)

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

# **do_protocol_asset_import**
> List[AssetTreeNode] do_protocol_asset_import(agent_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, file_info=file_info)

Do protocol asset import

### Example


```python
from or_rest_client import AuthenticatedApiClient, AgentApi
from or_rest_client.models.asset_tree_node import AssetTreeNode
from or_rest_client.models.file_info import FileInfo
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
api_instance = AgentApi(client)
agent_id = 'agent_id_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)
file_info = or_rest_client.FileInfo() # FileInfo |  (optional)

try:
    # Do protocol asset import
    api_response = api_instance.do_protocol_asset_import(agent_id, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, realm=realm, file_info=file_info)
    print("The response of AgentApi->do_protocol_asset_import:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AgentApi->do_protocol_asset_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 
 **file_info** | [**FileInfo**](FileInfo.md)|  | [optional] 

### Return type

[**List[AssetTreeNode]**](AssetTreeNode.md)

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

# **do_protocol_instance_discovery**
> List[AgentObjectObjectObject] do_protocol_instance_discovery(agent_type, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, realm=realm)

Do protocol instance discovery

### Example


```python
from or_rest_client import AuthenticatedApiClient, AgentApi
from or_rest_client.models.agent_object_object_object import AgentObjectObjectObject
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
api_instance = AgentApi(client)
agent_type = 'agent_type_example' # str | 
authorization = 'authorization_example' # str |  (optional)
x_forwarded_proto = 'x_forwarded_proto_example' # str |  (optional)
x_forwarded_host = 'x_forwarded_host_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)

try:
    # Do protocol instance discovery
    api_response = api_instance.do_protocol_instance_discovery(agent_type, authorization=authorization, x_forwarded_proto=x_forwarded_proto, x_forwarded_host=x_forwarded_host, parent_id=parent_id, realm=realm)
    print("The response of AgentApi->do_protocol_instance_discovery:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AgentApi->do_protocol_instance_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_type** | **str**|  | 
 **authorization** | **str**|  | [optional] 
 **x_forwarded_proto** | **str**|  | [optional] 
 **x_forwarded_host** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 

### Return type

[**List[AgentObjectObjectObject]**](AgentObjectObjectObject.md)

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

