# ArrayPredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 
**index** | **int** |  | [optional] 
**length_equals** | **int** |  | [optional] 
**length_greater_than** | **int** |  | [optional] 
**length_less_than** | **int** |  | [optional] 
**negated** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.array_predicate import ArrayPredicate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayPredicate from a JSON string
array_predicate_instance = ArrayPredicate.from_json(json)
# print the JSON string representation of the object
print(ArrayPredicate.to_json())

# convert the object into a dict
array_predicate_dict = array_predicate_instance.to_dict()
# create an instance of ArrayPredicate from a dict
array_predicate_from_dict = ArrayPredicate.from_dict(array_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


