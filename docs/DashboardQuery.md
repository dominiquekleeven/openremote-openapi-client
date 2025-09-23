# DashboardQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select** | [**Select**](Select.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**names** | [**List[StringPredicate]**](StringPredicate.md) |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**realm** | [**RealmPredicate**](RealmPredicate.md) |  | [optional] 
**start** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from or_rest_client.models.dashboard_query import DashboardQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardQuery from a JSON string
dashboard_query_instance = DashboardQuery.from_json(json)
# print the JSON string representation of the object
print(DashboardQuery.to_json())

# convert the object into a dict
dashboard_query_dict = dashboard_query_instance.to_dict()
# create an instance of DashboardQuery from a dict
dashboard_query_from_dict = DashboardQuery.from_dict(dashboard_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


