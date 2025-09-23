# ManagerAppConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_locales** | **bool** |  | [optional] 
**languages** | **Dict[str, str]** |  | [optional] 
**realms** | [**Dict[str, ManagerAppRealmConfig]**](ManagerAppRealmConfig.md) |  | [optional] 
**pages** | **Dict[str, object]** |  | [optional] 
**manager** | [**ManagerConfig**](ManagerConfig.md) |  | [optional] 

## Example

```python
from or_rest_client.models.manager_app_config import ManagerAppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerAppConfig from a JSON string
manager_app_config_instance = ManagerAppConfig.from_json(json)
# print the JSON string representation of the object
print(ManagerAppConfig.to_json())

# convert the object into a dict
manager_app_config_dict = manager_app_config_instance.to_dict()
# create an instance of ManagerAppConfig from a dict
manager_app_config_from_dict = ManagerAppConfig.from_dict(manager_app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


