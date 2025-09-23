# AssetDatapointQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_timestamp** | **int** |  | [optional] 
**to_timestamp** | **int** |  | [optional] 
**from_time** | **datetime** |  | [optional] 
**to_time** | **datetime** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from openremote_openapi_client.models.asset_datapoint_query import AssetDatapointQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDatapointQuery from a JSON string
asset_datapoint_query_instance = AssetDatapointQuery.from_json(json)
# print the JSON string representation of the object
print(AssetDatapointQuery.to_json())

# convert the object into a dict
asset_datapoint_query_dict = asset_datapoint_query_instance.to_dict()
# create an instance of AssetDatapointQuery from a dict
asset_datapoint_query_from_dict = AssetDatapointQuery.from_dict(asset_datapoint_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


