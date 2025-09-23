# RealmRuleset


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
**realm** | **str** |  | [optional] 
**access_public_read** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.realm_ruleset import RealmRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of RealmRuleset from a JSON string
realm_ruleset_instance = RealmRuleset.from_json(json)
# print the JSON string representation of the object
print(RealmRuleset.to_json())

# convert the object into a dict
realm_ruleset_dict = realm_ruleset_instance.to_dict()
# create an instance of RealmRuleset from a dict
realm_ruleset_from_dict = RealmRuleset.from_dict(realm_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


