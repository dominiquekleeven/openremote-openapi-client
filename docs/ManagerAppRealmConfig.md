# ManagerAppRealmConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_title** | **str** |  | [optional] 
**styles** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**logo_mobile** | **str** |  | [optional] 
**favicon** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**headers** | **List[str]** |  | [optional] 
**notifications** | [**ManagerAppRealmNotificationConfig**](ManagerAppRealmNotificationConfig.md) |  | [optional] 

## Example

```python
from or_rest_client.models.manager_app_realm_config import ManagerAppRealmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerAppRealmConfig from a JSON string
manager_app_realm_config_instance = ManagerAppRealmConfig.from_json(json)
# print the JSON string representation of the object
print(ManagerAppRealmConfig.to_json())

# convert the object into a dict
manager_app_realm_config_dict = manager_app_realm_config_instance.to_dict()
# create an instance of ManagerAppRealmConfig from a dict
manager_app_realm_config_from_dict = ManagerAppRealmConfig.from_dict(manager_app_realm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


