# AssetDatapointIntervalQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**gap_fill** | **bool** |  | [optional] 
**formula** | **str** |  | [optional] 

## Example

```python
from or_rest_client.models.asset_datapoint_interval_query import AssetDatapointIntervalQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDatapointIntervalQuery from a JSON string
asset_datapoint_interval_query_instance = AssetDatapointIntervalQuery.from_json(json)
# print the JSON string representation of the object
print(AssetDatapointIntervalQuery.to_json())

# convert the object into a dict
asset_datapoint_interval_query_dict = asset_datapoint_interval_query_instance.to_dict()
# create an instance of AssetDatapointIntervalQuery from a dict
asset_datapoint_interval_query_from_dict = AssetDatapointIntervalQuery.from_dict(asset_datapoint_interval_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


