# SentNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | 
**target** | **str** |  | 
**target_id** | **str** |  | 
**source** | **str** |  | 
**source_id** | **str** |  | [optional] 
**message** | [**AbstractNotificationMessage**](AbstractNotificationMessage.md) |  | [optional] 
**error** | **str** |  | [optional] 
**sent_on** | **datetime** |  | [optional] 
**delivered_on** | **datetime** |  | [optional] 
**acknowledged_on** | **datetime** |  | [optional] 
**acknowledgement** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.sent_notification import SentNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SentNotification from a JSON string
sent_notification_instance = SentNotification.from_json(json)
# print the JSON string representation of the object
print(SentNotification.to_json())

# convert the object into a dict
sent_notification_dict = sent_notification_instance.to_dict()
# create an instance of SentNotification from a dict
sent_notification_from_dict = SentNotification.from_dict(sent_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


