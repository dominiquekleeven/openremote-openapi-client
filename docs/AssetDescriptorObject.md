# AssetDescriptorObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**colour** | **str** |  | [optional] 
**dynamic** | **bool** |  | [optional] 
**descriptor_type** | **str** |  | 

## Example

```python
from openremote_openapi_client.models.asset_descriptor_object import AssetDescriptorObject

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDescriptorObject from a JSON string
asset_descriptor_object_instance = AssetDescriptorObject.from_json(json)
# print the JSON string representation of the object
print(AssetDescriptorObject.to_json())

# convert the object into a dict
asset_descriptor_object_dict = asset_descriptor_object_instance.to_dict()
# create an instance of AssetDescriptorObject from a dict
asset_descriptor_object_from_dict = AssetDescriptorObject.from_dict(asset_descriptor_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


