# GlobalRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**rules** | **str** |  | [optional] 
**lang** | **str** |  | 
**meta** | **Dict[str, object]** |  | [optional] 
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from or_rest_client.models.global_ruleset import GlobalRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalRuleset from a JSON string
global_ruleset_instance = GlobalRuleset.from_json(json)
# print the JSON string representation of the object
print(GlobalRuleset.to_json())

# convert the object into a dict
global_ruleset_dict = global_ruleset_instance.to_dict()
# create an instance of GlobalRuleset from a dict
global_ruleset_from_dict = GlobalRuleset.from_dict(global_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


