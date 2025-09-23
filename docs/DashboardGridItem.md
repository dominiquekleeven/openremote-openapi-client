# DashboardGridItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 
**w** | **int** |  | [optional] 
**h** | **int** |  | [optional] 
**min_h** | **int** |  | [optional] 
**min_w** | **int** |  | [optional] 
**min_pixel_h** | **int** |  | [optional] 
**min_pixel_w** | **int** |  | [optional] 
**no_resize** | **bool** |  | [optional] 
**no_move** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.dashboard_grid_item import DashboardGridItem

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardGridItem from a JSON string
dashboard_grid_item_instance = DashboardGridItem.from_json(json)
# print the JSON string representation of the object
print(DashboardGridItem.to_json())

# convert the object into a dict
dashboard_grid_item_dict = dashboard_grid_item_instance.to_dict()
# create an instance of DashboardGridItem from a dict
dashboard_grid_item_from_dict = DashboardGridItem.from_dict(dashboard_grid_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


