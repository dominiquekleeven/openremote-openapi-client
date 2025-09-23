# NodeSocket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.node_socket import NodeSocket

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSocket from a JSON string
node_socket_instance = NodeSocket.from_json(json)
# print the JSON string representation of the object
print(NodeSocket.to_json())

# convert the object into a dict
node_socket_dict = node_socket_instance.to_dict()
# create an instance of NodeSocket from a dict
node_socket_from_dict = NodeSocket.from_dict(node_socket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


