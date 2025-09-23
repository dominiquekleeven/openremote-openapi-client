# Pattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regexp** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.pattern import Pattern

# TODO update the JSON string below
json = "{}"
# create an instance of Pattern from a JSON string
pattern_instance = Pattern.from_json(json)
# print the JSON string representation of the object
print(Pattern.to_json())

# convert the object into a dict
pattern_dict = pattern_instance.to_dict()
# create an instance of Pattern from a dict
pattern_from_dict = Pattern.from_dict(pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


