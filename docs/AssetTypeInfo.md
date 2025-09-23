# AssetTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_descriptor** | [**AssetDescriptorObject**](AssetDescriptorObject.md) |  | [optional] 
**attribute_descriptors** | [**List[AttributeDescriptorObject]**](AttributeDescriptorObject.md) |  | [optional] 
**meta_item_descriptors** | [**List[MetaItemDescriptorObject]**](MetaItemDescriptorObject.md) |  | [optional] 
**value_descriptors** | [**List[ValueDescriptorObject]**](ValueDescriptorObject.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.asset_type_info import AssetTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeInfo from a JSON string
asset_type_info_instance = AssetTypeInfo.from_json(json)
# print the JSON string representation of the object
print(AssetTypeInfo.to_json())

# convert the object into a dict
asset_type_info_dict = asset_type_info_instance.to_dict()
# create an instance of AssetTypeInfo from a dict
asset_type_info_from_dict = AssetTypeInfo.from_dict(asset_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


