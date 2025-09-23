# ConsoleRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**version** | **str** |  | 
**platform** | **str** |  | 
**providers** | [**Dict[str, ConsoleProvider]**](ConsoleProvider.md) |  | 
**model** | **str** |  | [optional] 
**apps** | **List[str]** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.console_registration import ConsoleRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleRegistration from a JSON string
console_registration_instance = ConsoleRegistration.from_json(json)
# print the JSON string representation of the object
print(ConsoleRegistration.to_json())

# convert the object into a dict
console_registration_dict = console_registration_instance.to_dict()
# create an instance of ConsoleRegistration from a dict
console_registration_from_dict = ConsoleRegistration.from_dict(console_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


