# RadialGeofencePredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **int** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**negated** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.radial_geofence_predicate import RadialGeofencePredicate

# TODO update the JSON string below
json = "{}"
# create an instance of RadialGeofencePredicate from a JSON string
radial_geofence_predicate_instance = RadialGeofencePredicate.from_json(json)
# print the JSON string representation of the object
print(RadialGeofencePredicate.to_json())

# convert the object into a dict
radial_geofence_predicate_dict = radial_geofence_predicate_instance.to_dict()
# create an instance of RadialGeofencePredicate from a dict
radial_geofence_predicate_from_dict = RadialGeofencePredicate.from_dict(radial_geofence_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


