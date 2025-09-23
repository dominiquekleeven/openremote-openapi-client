# AttributeRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The asset identifier | [optional] 
**name** | **str** | The attribute name | 

## Example

```python
from openremote_openapi_client.models.attribute_ref import AttributeRef

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeRef from a JSON string
attribute_ref_instance = AttributeRef.from_json(json)
# print the JSON string representation of the object
print(AttributeRef.to_json())

# convert the object into a dict
attribute_ref_dict = attribute_ref_instance.to_dict()
# create an instance of AttributeRef from a dict
attribute_ref_from_dict = AttributeRef.from_dict(attribute_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


