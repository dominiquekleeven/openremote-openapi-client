# AssetRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**rules** | **str** |  | [optional] 
**lang** | **str** |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**access_public_read** | **bool** |  | [optional] 
**realm** | **str** |  | [optional] 

## Example

```python
from or_rest_client.models.asset_ruleset import AssetRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRuleset from a JSON string
asset_ruleset_instance = AssetRuleset.from_json(json)
# print the JSON string representation of the object
print(AssetRuleset.to_json())

# convert the object into a dict
asset_ruleset_dict = asset_ruleset_instance.to_dict()
# create an instance of AssetRuleset from a dict
asset_ruleset_from_dict = AssetRuleset.from_dict(asset_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


