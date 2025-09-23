# PushNotificationButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**action** | [**PushNotificationAction**](PushNotificationAction.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.push_notification_button import PushNotificationButton

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationButton from a JSON string
push_notification_button_instance = PushNotificationButton.from_json(json)
# print the JSON string representation of the object
print(PushNotificationButton.to_json())

# convert the object into a dict
push_notification_button_dict = push_notification_button_instance.to_dict()
# create an instance of PushNotificationButton from a dict
push_notification_button_from_dict = PushNotificationButton.from_dict(push_notification_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


