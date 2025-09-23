# AlarmAssetLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**parent_asset_name** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.alarm_asset_link import AlarmAssetLink

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmAssetLink from a JSON string
alarm_asset_link_instance = AlarmAssetLink.from_json(json)
# print the JSON string representation of the object
print(AlarmAssetLink.to_json())

# convert the object into a dict
alarm_asset_link_dict = alarm_asset_link_instance.to_dict()
# create an instance of AlarmAssetLink from a dict
alarm_asset_link_from_dict = AlarmAssetLink.from_dict(alarm_asset_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


