# AttributeObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ValueDescriptorObject**](ValueDescriptorObject.md) |  | [optional] 
**value** | **object** |  | [optional] 
**name** | **str** |  | 
**meta** | [**AttributeObjectMeta**](AttributeObjectMeta.md) |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from or_rest_client.models.attribute_object import AttributeObject

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeObject from a JSON string
attribute_object_instance = AttributeObject.from_json(json)
# print the JSON string representation of the object
print(AttributeObject.to_json())

# convert the object into a dict
attribute_object_dict = attribute_object_instance.to_dict()
# create an instance of AttributeObject from a dict
attribute_object_from_dict = AttributeObject.from_dict(attribute_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


