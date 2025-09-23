# EmailNotificationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**Recipient**](Recipient.md) |  | [optional] 
**reply_to** | [**Recipient**](Recipient.md) |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**to** | [**List[Recipient]**](Recipient.md) |  | [optional] 
**cc** | [**List[Recipient]**](Recipient.md) |  | [optional] 
**bcc** | [**List[Recipient]**](Recipient.md) |  | [optional] 

## Example

```python
from or_rest_client.models.email_notification_message import EmailNotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationMessage from a JSON string
email_notification_message_instance = EmailNotificationMessage.from_json(json)
# print the JSON string representation of the object
print(EmailNotificationMessage.to_json())

# convert the object into a dict
email_notification_message_dict = email_notification_message_instance.to_dict()
# create an instance of EmailNotificationMessage from a dict
email_notification_message_from_dict = EmailNotificationMessage.from_dict(email_notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


