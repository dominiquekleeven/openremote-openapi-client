# AllowedValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_value_names** | **List[str]** |  | [optional] 
**allowed_values** | **List[object]** |  | [optional] 

## Example

```python
from or_rest_client.models.allowed_values import AllowedValues

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedValues from a JSON string
allowed_values_instance = AllowedValues.from_json(json)
# print the JSON string representation of the object
print(AllowedValues.to_json())

# convert the object into a dict
allowed_values_dict = allowed_values_instance.to_dict()
# create an instance of AllowedValues from a dict
allowed_values_from_dict = AllowedValues.from_dict(allowed_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


