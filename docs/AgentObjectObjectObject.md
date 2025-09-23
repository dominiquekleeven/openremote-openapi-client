# AgentObjectObjectObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**name** | **str** |  | 
**access_public_read** | **bool** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**realm** | **str** |  | 
**type** | **str** |  | [optional] 
**path** | **List[str]** |  | [optional] 
**attributes** | [**AssetObjectAttributes**](AssetObjectAttributes.md) |  | [optional] 

## Example

```python
from or_rest_client.models.agent_object_object_object import AgentObjectObjectObject

# TODO update the JSON string below
json = "{}"
# create an instance of AgentObjectObjectObject from a JSON string
agent_object_object_object_instance = AgentObjectObjectObject.from_json(json)
# print the JSON string representation of the object
print(AgentObjectObjectObject.to_json())

# convert the object into a dict
agent_object_object_object_dict = agent_object_object_object_instance.to_dict()
# create an instance of AgentObjectObjectObject from a dict
agent_object_object_object_from_dict = AgentObjectObjectObject.from_dict(agent_object_object_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


