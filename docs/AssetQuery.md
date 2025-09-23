# AssetQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recursive** | **bool** |  | [optional] 
**select** | [**Select**](Select.md) |  | [optional] 
**access** | **str** |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**names** | [**List[StringPredicate]**](StringPredicate.md) |  | [optional] 
**parents** | [**List[ParentPredicate]**](ParentPredicate.md) |  | [optional] 
**paths** | [**List[PathPredicate]**](PathPredicate.md) |  | [optional] 
**realm** | [**RealmPredicate**](RealmPredicate.md) |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**attributes** | [**LogicGroupAttributePredicate**](LogicGroupAttributePredicate.md) |  | [optional] 
**order_by** | [**OrderBy**](OrderBy.md) |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from or_rest_client.models.asset_query import AssetQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AssetQuery from a JSON string
asset_query_instance = AssetQuery.from_json(json)
# print the JSON string representation of the object
print(AssetQuery.to_json())

# convert the object into a dict
asset_query_dict = asset_query_instance.to_dict()
# create an instance of AssetQuery from a dict
asset_query_from_dict = AssetQuery.from_dict(asset_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


