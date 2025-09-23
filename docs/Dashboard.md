# Dashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**realm** | **str** |  | 
**version** | **int** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**access** | **str** |  | [optional] 
**display_name** | **str** |  | 
**template** | [**DashboardTemplate**](DashboardTemplate.md) |  | 

## Example

```python
from openremote_openapi_client.models.dashboard import Dashboard

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboard from a JSON string
dashboard_instance = Dashboard.from_json(json)
# print the JSON string representation of the object
print(Dashboard.to_json())

# convert the object into a dict
dashboard_dict = dashboard_instance.to_dict()
# create an instance of Dashboard from a dict
dashboard_from_dict = Dashboard.from_dict(dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


