# DatapointPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**oldest_timestamp** | **int** |  | [optional] 
**latest_timestamp** | **int** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.datapoint_period import DatapointPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of DatapointPeriod from a JSON string
datapoint_period_instance = DatapointPeriod.from_json(json)
# print the JSON string representation of the object
print(DatapointPeriod.to_json())

# convert the object into a dict
datapoint_period_dict = datapoint_period_instance.to_dict()
# create an instance of DatapointPeriod from a dict
datapoint_period_from_dict = DatapointPeriod.from_dict(datapoint_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


