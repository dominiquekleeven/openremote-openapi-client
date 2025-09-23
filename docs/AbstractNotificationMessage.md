# AbstractNotificationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 

## Example

```python
from or_rest_client.models.abstract_notification_message import AbstractNotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractNotificationMessage from a JSON string
abstract_notification_message_instance = AbstractNotificationMessage.from_json(json)
# print the JSON string representation of the object
print(AbstractNotificationMessage.to_json())

# convert the object into a dict
abstract_notification_message_dict = abstract_notification_message_instance.to_dict()
# create an instance of AbstractNotificationMessage from a dict
abstract_notification_message_from_dict = AbstractNotificationMessage.from_dict(abstract_notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


