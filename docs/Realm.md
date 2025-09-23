# Realm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**not_before** | **float** |  | [optional] 
**password_policy** | **List[str]** |  | [optional] 
**reset_password_allowed** | **bool** |  | [optional] 
**duplicate_emails_allowed** | **bool** |  | [optional] 
**remember_me** | **bool** |  | [optional] 
**registration_allowed** | **bool** |  | [optional] 
**registration_email_as_username** | **bool** |  | [optional] 
**verify_email** | **bool** |  | [optional] 
**login_with_email** | **bool** |  | [optional] 
**login_theme** | **str** |  | [optional] 
**account_theme** | **str** |  | [optional] 
**admin_theme** | **str** |  | [optional] 
**email_theme** | **str** |  | [optional] 
**access_token_lifespan** | **int** |  | [optional] 
**realm_roles** | [**List[RealmRole]**](RealmRole.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.realm import Realm

# TODO update the JSON string below
json = "{}"
# create an instance of Realm from a JSON string
realm_instance = Realm.from_json(json)
# print the JSON string representation of the object
print(Realm.to_json())

# convert the object into a dict
realm_dict = realm_instance.to_dict()
# create an instance of Realm from a dict
realm_from_dict = Realm.from_dict(realm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


