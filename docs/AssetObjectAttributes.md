# AssetObjectAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate** | [**Dict[str, AttributeObject]**](AttributeObject.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.asset_object_attributes import AssetObjectAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AssetObjectAttributes from a JSON string
asset_object_attributes_instance = AssetObjectAttributes.from_json(json)
# print the JSON string representation of the object
print(AssetObjectAttributes.to_json())

# convert the object into a dict
asset_object_attributes_dict = asset_object_attributes_instance.to_dict()
# create an instance of AssetObjectAttributes from a dict
asset_object_attributes_from_dict = AssetObjectAttributes.from_dict(asset_object_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


