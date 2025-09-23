# ConsoleProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**requires_permission** | **bool** |  | [optional] 
**has_permission** | **bool** |  | [optional] 
**success** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from or_rest_client.models.console_provider import ConsoleProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleProvider from a JSON string
console_provider_instance = ConsoleProvider.from_json(json)
# print the JSON string representation of the object
print(ConsoleProvider.to_json())

# convert the object into a dict
console_provider_dict = console_provider_instance.to_dict()
# create an instance of ConsoleProvider from a dict
console_provider_from_dict = ConsoleProvider.from_dict(console_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


