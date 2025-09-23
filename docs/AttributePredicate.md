# AttributePredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**StringPredicate**](StringPredicate.md) |  | [optional] 
**negated** | **bool** |  | [optional] 
**path** | **List[object]** |  | [optional] 
**value** | [**ValuePredicate**](ValuePredicate.md) |  | [optional] 
**meta** | [**List[NameValuePredicate]**](NameValuePredicate.md) |  | [optional] 
**previous_value** | [**ValuePredicate**](ValuePredicate.md) |  | [optional] 
**timestamp_older_than** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.attribute_predicate import AttributePredicate

# TODO update the JSON string below
json = "{}"
# create an instance of AttributePredicate from a JSON string
attribute_predicate_instance = AttributePredicate.from_json(json)
# print the JSON string representation of the object
print(AttributePredicate.to_json())

# convert the object into a dict
attribute_predicate_dict = attribute_predicate_instance.to_dict()
# create an instance of AttributePredicate from a dict
attribute_predicate_from_dict = AttributePredicate.from_dict(attribute_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


