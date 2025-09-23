# UserAssetLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**parent_asset_name** | **str** |  | [optional] 
**user_full_name** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.user_asset_link import UserAssetLink

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssetLink from a JSON string
user_asset_link_instance = UserAssetLink.from_json(json)
# print the JSON string representation of the object
print(UserAssetLink.to_json())

# convert the object into a dict
user_asset_link_dict = user_asset_link_instance.to_dict()
# create an instance of UserAssetLink from a dict
user_asset_link_from_dict = UserAssetLink.from_dict(user_asset_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


