# AttributeObjectMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate** | [**Dict[str, MetaItemObject]**](MetaItemObject.md) |  | [optional] 

## Example

```python
from or_rest_client.models.attribute_object_meta import AttributeObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeObjectMeta from a JSON string
attribute_object_meta_instance = AttributeObjectMeta.from_json(json)
# print the JSON string representation of the object
print(AttributeObjectMeta.to_json())

# convert the object into a dict
attribute_object_meta_dict = attribute_object_meta_instance.to_dict()
# create an instance of AttributeObjectMeta from a dict
attribute_object_meta_from_dict = AttributeObjectMeta.from_dict(attribute_object_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


