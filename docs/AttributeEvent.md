# AttributeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_state** | [**AttributeState**](AttributeState.md) |  | [optional] 
**ref** | [**AttributeRef**](AttributeRef.md) |  | [optional] 
**value** | **object** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**message_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**realm** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**old_value** | **object** |  | [optional] 
**old_value_timestamp** | **int** |  | [optional] 
**path** | **List[str]** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**asset_type** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**type** | [**ValueDescriptor**](ValueDescriptor.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.attribute_event import AttributeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeEvent from a JSON string
attribute_event_instance = AttributeEvent.from_json(json)
# print the JSON string representation of the object
print(AttributeEvent.to_json())

# convert the object into a dict
attribute_event_dict = attribute_event_instance.to_dict()
# create an instance of AttributeEvent from a dict
attribute_event_from_dict = AttributeEvent.from_dict(attribute_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


