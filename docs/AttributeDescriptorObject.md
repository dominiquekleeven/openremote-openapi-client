# AttributeDescriptorObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**ValueDescriptorObject**](ValueDescriptorObject.md) |  | [optional] 
**constraints** | [**List[ValueConstraint]**](ValueConstraint.md) |  | [optional] 
**format** | [**ValueFormat**](ValueFormat.md) |  | [optional] 
**units** | **List[str]** |  | [optional] 
**meta** | [**AttributeObjectMeta**](AttributeObjectMeta.md) |  | [optional] 
**optional** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.attribute_descriptor_object import AttributeDescriptorObject

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDescriptorObject from a JSON string
attribute_descriptor_object_instance = AttributeDescriptorObject.from_json(json)
# print the JSON string representation of the object
print(AttributeDescriptorObject.to_json())

# convert the object into a dict
attribute_descriptor_object_dict = attribute_descriptor_object_instance.to_dict()
# create an instance of AttributeDescriptorObject from a dict
attribute_descriptor_object_from_dict = AttributeDescriptorObject.from_dict(attribute_descriptor_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


