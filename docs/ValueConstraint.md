# ValueConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from or_rest_client.models.value_constraint import ValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ValueConstraint from a JSON string
value_constraint_instance = ValueConstraint.from_json(json)
# print the JSON string representation of the object
print(ValueConstraint.to_json())

# convert the object into a dict
value_constraint_dict = value_constraint_instance.to_dict()
# create an instance of ValueConstraint from a dict
value_constraint_from_dict = ValueConstraint.from_dict(value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


