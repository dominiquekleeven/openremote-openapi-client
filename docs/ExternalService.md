# ExternalService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm** | **str** |  | [optional] [readonly] 
**is_global** | **bool** |  | [optional] [readonly] 
**service_id** | **str** |  | 
**instance_id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**label** | **str** |  | 
**homepage_url** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from or_rest_client.models.external_service import ExternalService

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalService from a JSON string
external_service_instance = ExternalService.from_json(json)
# print the JSON string representation of the object
print(ExternalService.to_json())

# convert the object into a dict
external_service_dict = external_service_instance.to_dict()
# create an instance of ExternalService from a dict
external_service_from_dict = ExternalService.from_dict(external_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


