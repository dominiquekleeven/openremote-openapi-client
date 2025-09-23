# ManagerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_url** | **str** |  | [optional] 
**keycloak_url** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**auto_login** | **bool** |  | [optional] 
**console_auto_enable** | **bool** |  | [optional] 
**load_icons** | **bool** |  | [optional] 
**polling_interval_millis** | **int** |  | [optional] 
**load_translations** | **List[str]** |  | [optional] 
**load_descriptors** | **bool** |  | [optional] 
**translations_load_path** | **str** |  | [optional] 
**skip_fallback_to_basic_auth** | **bool** |  | [optional] 
**apply_config_to_admin** | **bool** |  | [optional] 
**auth** | **str** |  | [optional] 
**credentials** | [**UsernamePassword**](UsernamePassword.md) |  | [optional] 
**event_provider_type** | **str** |  | [optional] 
**map_type** | **str** |  | [optional] 
**configure_translations_options** | **object** |  | [optional] 
**basic_login_provider** | **object** |  | [optional] 
**default_language** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.manager_config import ManagerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerConfig from a JSON string
manager_config_instance = ManagerConfig.from_json(json)
# print the JSON string representation of the object
print(ManagerConfig.to_json())

# convert the object into a dict
manager_config_dict = manager_config_instance.to_dict()
# create an instance of ManagerConfig from a dict
manager_config_from_dict = ManagerConfig.from_dict(manager_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


