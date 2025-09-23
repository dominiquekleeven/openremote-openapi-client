# BooleanPredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | [optional] 

## Example

```python
from or_rest_client.models.boolean_predicate import BooleanPredicate

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanPredicate from a JSON string
boolean_predicate_instance = BooleanPredicate.from_json(json)
# print the JSON string representation of the object
print(BooleanPredicate.to_json())

# convert the object into a dict
boolean_predicate_dict = boolean_predicate_instance.to_dict()
# create an instance of BooleanPredicate from a dict
boolean_predicate_from_dict = BooleanPredicate.from_dict(boolean_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


