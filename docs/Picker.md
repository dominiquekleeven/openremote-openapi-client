# Picker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**options** | [**List[Option]**](Option.md) |  | [optional] 

## Example

```python
from or_rest_client.models.picker import Picker

# TODO update the JSON string below
json = "{}"
# create an instance of Picker from a JSON string
picker_instance = Picker.from_json(json)
# print the JSON string representation of the object
print(Picker.to_json())

# convert the object into a dict
picker_dict = picker_instance.to_dict()
# create an instance of Picker from a dict
picker_from_dict = Picker.from_dict(picker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


