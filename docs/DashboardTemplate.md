# DashboardTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**columns** | **int** |  | [optional] 
**max_screen_width** | **int** |  | [optional] 
**refresh_interval** | **str** |  | [optional] 
**screen_presets** | [**List[DashboardScreenPreset]**](DashboardScreenPreset.md) |  | 
**widgets** | [**List[DashboardWidget]**](DashboardWidget.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.dashboard_template import DashboardTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardTemplate from a JSON string
dashboard_template_instance = DashboardTemplate.from_json(json)
# print the JSON string representation of the object
print(DashboardTemplate.to_json())

# convert the object into a dict
dashboard_template_dict = dashboard_template_instance.to_dict()
# create an instance of DashboardTemplate from a dict
dashboard_template_from_dict = DashboardTemplate.from_dict(dashboard_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


