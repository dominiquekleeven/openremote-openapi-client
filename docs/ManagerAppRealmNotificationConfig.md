# ManagerAppRealmNotificationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languages** | **List[str]** |  | [optional] 
**default_language** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.manager_app_realm_notification_config import ManagerAppRealmNotificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerAppRealmNotificationConfig from a JSON string
manager_app_realm_notification_config_instance = ManagerAppRealmNotificationConfig.from_json(json)
# print the JSON string representation of the object
print(ManagerAppRealmNotificationConfig.to_json())

# convert the object into a dict
manager_app_realm_notification_config_dict = manager_app_realm_notification_config_instance.to_dict()
# create an instance of ManagerAppRealmNotificationConfig from a dict
manager_app_realm_notification_config_from_dict = ManagerAppRealmNotificationConfig.from_dict(manager_app_realm_notification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


