# UserQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm_predicate** | [**RealmPredicate**](RealmPredicate.md) |  | [optional] 
**assets** | **List[str]** |  | [optional] 
**path_predicate** | [**PathPredicate**](PathPredicate.md) |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**select** | [**Select**](Select.md) |  | [optional] 
**usernames** | [**List[StringPredicate]**](StringPredicate.md) |  | [optional] 
**attributes** | [**List[AttributeValuePredicate]**](AttributeValuePredicate.md) |  | [optional] 
**client_roles** | [**List[StringPredicate]**](StringPredicate.md) |  | [optional] 
**realm_roles** | [**List[StringPredicate]**](StringPredicate.md) |  | [optional] 
**service_users** | **bool** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order_by** | [**OrderBy**](OrderBy.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.user_query import UserQuery

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuery from a JSON string
user_query_instance = UserQuery.from_json(json)
# print the JSON string representation of the object
print(UserQuery.to_json())

# convert the object into a dict
user_query_dict = user_query_instance.to_dict()
# create an instance of UserQuery from a dict
user_query_from_dict = UserQuery.from_dict(user_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


