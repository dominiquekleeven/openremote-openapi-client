# AgentDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_discovery** | **bool** |  | [optional] 
**asset_import** | **bool** |  | [optional] 
**agent_link_type** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.agent_descriptor import AgentDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDescriptor from a JSON string
agent_descriptor_instance = AgentDescriptor.from_json(json)
# print the JSON string representation of the object
print(AgentDescriptor.to_json())

# convert the object into a dict
agent_descriptor_dict = agent_descriptor_instance.to_dict()
# create an instance of AgentDescriptor from a dict
agent_descriptor_from_dict = AgentDescriptor.from_dict(agent_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


