# Alarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**content** | **str** |  | [optional] 
**severity** | **str** |  | 
**assignee_id** | **str** |  | [optional] 
**realm** | **str** |  | 
**status** | **str** |  | 
**source_id** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from or_rest_client.models.alarm import Alarm

# TODO update the JSON string below
json = "{}"
# create an instance of Alarm from a JSON string
alarm_instance = Alarm.from_json(json)
# print the JSON string representation of the object
print(Alarm.to_json())

# convert the object into a dict
alarm_dict = alarm_instance.to_dict()
# create an instance of Alarm from a dict
alarm_from_dict = Alarm.from_dict(alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


