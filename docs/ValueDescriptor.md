# ValueDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**constraints** | [**List[ValueConstraint]**](ValueConstraint.md) |  | [optional] 
**format** | [**ValueFormat**](ValueFormat.md) |  | [optional] 
**units** | **List[str]** |  | [optional] 
**array_dimensions** | **int** |  | [optional] 
**meta_use_only** | **bool** |  | [optional] 
**json_type** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.value_descriptor import ValueDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ValueDescriptor from a JSON string
value_descriptor_instance = ValueDescriptor.from_json(json)
# print the JSON string representation of the object
print(ValueDescriptor.to_json())

# convert the object into a dict
value_descriptor_dict = value_descriptor_instance.to_dict()
# create an instance of ValueDescriptor from a dict
value_descriptor_from_dict = ValueDescriptor.from_dict(value_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


