# DateTimePredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**range_value** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.date_time_predicate import DateTimePredicate

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimePredicate from a JSON string
date_time_predicate_instance = DateTimePredicate.from_json(json)
# print the JSON string representation of the object
print(DateTimePredicate.to_json())

# convert the object into a dict
date_time_predicate_dict = date_time_predicate_instance.to_dict()
# create an instance of DateTimePredicate from a dict
date_time_predicate_from_dict = DateTimePredicate.from_dict(date_time_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


