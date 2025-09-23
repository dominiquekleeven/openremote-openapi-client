# AttributeState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | [**AttributeRef**](AttributeRef.md) |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.attribute_state import AttributeState

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeState from a JSON string
attribute_state_instance = AttributeState.from_json(json)
# print the JSON string representation of the object
print(AttributeState.to_json())

# convert the object into a dict
attribute_state_dict = attribute_state_instance.to_dict()
# create an instance of AttributeState from a dict
attribute_state_from_dict = AttributeState.from_dict(attribute_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


