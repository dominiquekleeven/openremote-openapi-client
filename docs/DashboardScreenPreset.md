# DashboardScreenPreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | 
**breakpoint** | **int** |  | [optional] 
**scaling_preset** | **str** |  | 
**redirect_dashboard_id** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.dashboard_screen_preset import DashboardScreenPreset

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScreenPreset from a JSON string
dashboard_screen_preset_instance = DashboardScreenPreset.from_json(json)
# print the JSON string representation of the object
print(DashboardScreenPreset.to_json())

# convert the object into a dict
dashboard_screen_preset_dict = dashboard_screen_preset_instance.to_dict()
# create an instance of DashboardScreenPreset from a dict
dashboard_screen_preset_from_dict = DashboardScreenPreset.from_dict(dashboard_screen_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


