# MapSourceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tiles** | **List[str]** |  | [optional] 
**bounds** | **List[float]** |  | [optional] 
**scheme** | **str** |  | [optional] 
**minzoom** | **int** |  | [optional] 
**maxzoom** | **int** |  | [optional] 
**attribution** | **str** |  | [optional] 
**custom** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.map_source_config import MapSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MapSourceConfig from a JSON string
map_source_config_instance = MapSourceConfig.from_json(json)
# print the JSON string representation of the object
print(MapSourceConfig.to_json())

# convert the object into a dict
map_source_config_dict = map_source_config_instance.to_dict()
# create an instance of MapSourceConfig from a dict
map_source_config_from_dict = MapSourceConfig.from_dict(map_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


