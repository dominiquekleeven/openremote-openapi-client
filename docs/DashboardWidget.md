# DashboardWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | 
**grid_item** | [**DashboardGridItem**](DashboardGridItem.md) |  | 
**widget_type_id** | **str** |  | 
**widget_config** | **object** |  | [optional] 

## Example

```python
from or_rest_client.models.dashboard_widget import DashboardWidget

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWidget from a JSON string
dashboard_widget_instance = DashboardWidget.from_json(json)
# print the JSON string representation of the object
print(DashboardWidget.to_json())

# convert the object into a dict
dashboard_widget_dict = dashboard_widget_instance.to_dict()
# create an instance of DashboardWidget from a dict
dashboard_widget_from_dict = DashboardWidget.from_dict(dashboard_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


