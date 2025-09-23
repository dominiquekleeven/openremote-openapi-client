# MetaMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate** | [**Dict[str, MetaItemObject]**](MetaItemObject.md) |  | [optional] 

## Example

```python
from or_rest_client.models.meta_map import MetaMap

# TODO update the JSON string below
json = "{}"
# create an instance of MetaMap from a JSON string
meta_map_instance = MetaMap.from_json(json)
# print the JSON string representation of the object
print(MetaMap.to_json())

# convert the object into a dict
meta_map_dict = meta_map_instance.to_dict()
# create an instance of MetaMap from a dict
meta_map_from_dict = MetaMap.from_dict(meta_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


