# AttributeMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate** | [**Dict[str, AttributeObject]**](AttributeObject.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.attribute_map import AttributeMap

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeMap from a JSON string
attribute_map_instance = AttributeMap.from_json(json)
# print the JSON string representation of the object
print(AttributeMap.to_json())

# convert the object into a dict
attribute_map_dict = attribute_map_instance.to_dict()
# create an instance of AttributeMap from a dict
attribute_map_from_dict = AttributeMap.from_dict(attribute_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


