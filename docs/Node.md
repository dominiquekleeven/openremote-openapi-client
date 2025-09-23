# Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | [**NodePosition**](NodePosition.md) |  | [optional] 
**size** | [**NodePosition**](NodePosition.md) |  | [optional] 
**internals** | [**List[NodeInternal]**](NodeInternal.md) |  | [optional] 
**inputs** | [**List[NodeSocket]**](NodeSocket.md) |  | [optional] 
**outputs** | [**List[NodeSocket]**](NodeSocket.md) |  | [optional] 
**display_character** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


