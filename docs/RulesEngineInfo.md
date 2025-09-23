# RulesEngineInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**compilation_error_count** | **int** |  | [optional] 
**execution_error_count** | **int** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.rules_engine_info import RulesEngineInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineInfo from a JSON string
rules_engine_info_instance = RulesEngineInfo.from_json(json)
# print the JSON string representation of the object
print(RulesEngineInfo.to_json())

# convert the object into a dict
rules_engine_info_dict = rules_engine_info_instance.to_dict()
# create an instance of RulesEngineInfo from a dict
rules_engine_info_from_dict = RulesEngineInfo.from_dict(rules_engine_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


