# GatewayAttributeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matcher** | [**AssetQuery**](AssetQuery.md) |  | [optional] 
**duration** | **str** |  | [optional] 
**delta** | **float** |  | [optional] 
**value_change** | **bool** |  | [optional] 
**skip_always** | **bool** |  | [optional] 
**duration_parsed_millis** | **int** |  | [optional] 

## Example

```python
from or_rest_client.models.gateway_attribute_filter import GatewayAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAttributeFilter from a JSON string
gateway_attribute_filter_instance = GatewayAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(GatewayAttributeFilter.to_json())

# convert the object into a dict
gateway_attribute_filter_dict = gateway_attribute_filter_instance.to_dict()
# create an instance of GatewayAttributeFilter from a dict
gateway_attribute_filter_from_dict = GatewayAttributeFilter.from_dict(gateway_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


