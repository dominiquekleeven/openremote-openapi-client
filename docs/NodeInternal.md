# NodeInternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**picker** | [**Picker**](Picker.md) |  | [optional] 
**value** | **object** |  | [optional] 
**break_type** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.node_internal import NodeInternal

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInternal from a JSON string
node_internal_instance = NodeInternal.from_json(json)
# print the JSON string representation of the object
print(NodeInternal.to_json())

# convert the object into a dict
node_internal_dict = node_internal_instance.to_dict()
# create an instance of NodeInternal from a dict
node_internal_from_dict = NodeInternal.from_dict(node_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


