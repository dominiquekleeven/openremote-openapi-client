# GeofenceDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**radius** | **int** |  | [optional] 
**http_method** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.geofence_definition import GeofenceDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceDefinition from a JSON string
geofence_definition_instance = GeofenceDefinition.from_json(json)
# print the JSON string representation of the object
print(GeofenceDefinition.to_json())

# convert the object into a dict
geofence_definition_dict = geofence_definition_instance.to_dict()
# create an instance of GeofenceDefinition from a dict
geofence_definition_from_dict = GeofenceDefinition.from_dict(geofence_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


