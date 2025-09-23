# GatewayAssetSyncRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_attributes** | **List[str]** |  | [optional] 
**exclude_attribute_meta** | **Dict[str, List[str]]** |  | [optional] 
**add_attribute_meta** | [**Dict[str, MetaMap]**](MetaMap.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.gateway_asset_sync_rule import GatewayAssetSyncRule

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAssetSyncRule from a JSON string
gateway_asset_sync_rule_instance = GatewayAssetSyncRule.from_json(json)
# print the JSON string representation of the object
print(GatewayAssetSyncRule.to_json())

# convert the object into a dict
gateway_asset_sync_rule_dict = gateway_asset_sync_rule_instance.to_dict()
# create an instance of GatewayAssetSyncRule from a dict
gateway_asset_sync_rule_from_dict = GatewayAssetSyncRule.from_dict(gateway_asset_sync_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


