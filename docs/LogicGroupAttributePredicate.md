# LogicGroupAttributePredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**items** | [**List[AttributePredicate]**](AttributePredicate.md) |  | [optional] 
**groups** | [**List[LogicGroupAttributePredicate]**](LogicGroupAttributePredicate.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.logic_group_attribute_predicate import LogicGroupAttributePredicate

# TODO update the JSON string below
json = "{}"
# create an instance of LogicGroupAttributePredicate from a JSON string
logic_group_attribute_predicate_instance = LogicGroupAttributePredicate.from_json(json)
# print the JSON string representation of the object
print(LogicGroupAttributePredicate.to_json())

# convert the object into a dict
logic_group_attribute_predicate_dict = logic_group_attribute_predicate_instance.to_dict()
# create an instance of LogicGroupAttributePredicate from a dict
logic_group_attribute_predicate_from_dict = LogicGroupAttributePredicate.from_dict(logic_group_attribute_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


