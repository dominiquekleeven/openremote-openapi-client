# AssetConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **List[str]** |  | [optional] 
**min_amount** | **str** |  | [optional] 
**parents** | [**List[ParentPredicate]**](ParentPredicate.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.asset_conditions import AssetConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AssetConditions from a JSON string
asset_conditions_instance = AssetConditions.from_json(json)
# print the JSON string representation of the object
print(AssetConditions.to_json())

# convert the object into a dict
asset_conditions_dict = asset_conditions_instance.to_dict()
# create an instance of AssetConditions from a dict
asset_conditions_from_dict = AssetConditions.from_dict(asset_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


