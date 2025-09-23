# PushNotificationAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**silent** | **bool** |  | [optional] 
**open_in_browser** | **bool** |  | [optional] 
**http_method** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.push_notification_action import PushNotificationAction

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationAction from a JSON string
push_notification_action_instance = PushNotificationAction.from_json(json)
# print the JSON string representation of the object
print(PushNotificationAction.to_json())

# convert the object into a dict
push_notification_action_dict = push_notification_action_instance.to_dict()
# create an instance of PushNotificationAction from a dict
push_notification_action_from_dict = PushNotificationAction.from_dict(push_notification_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


