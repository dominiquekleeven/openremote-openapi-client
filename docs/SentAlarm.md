# SentAlarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**realm** | **str** |  | 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**severity** | **str** |  | 
**status** | **str** |  | 
**source** | **str** |  | 
**source_id** | **str** |  | [optional] 
**source_username** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**acknowledged_on** | **datetime** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**assignee_id** | **str** |  | [optional] 
**assignee_username** | **str** |  | [optional] 
**asset** | [**List[AssetObject]**](AssetObject.md) |  | [optional] 

## Example

```python
from or_rest_client.models.sent_alarm import SentAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of SentAlarm from a JSON string
sent_alarm_instance = SentAlarm.from_json(json)
# print the JSON string representation of the object
print(SentAlarm.to_json())

# convert the object into a dict
sent_alarm_dict = sent_alarm_instance.to_dict()
# create an instance of SentAlarm from a dict
sent_alarm_from_dict = SentAlarm.from_dict(sent_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


