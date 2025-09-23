# ValueFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_grouping** | **bool** |  | [optional] 
**minimum_integer_digits** | **int** |  | [optional] 
**minimum_fraction_digits** | **int** |  | [optional] 
**maximum_fraction_digits** | **int** |  | [optional] 
**minimum_significant_digits** | **int** |  | [optional] 
**maximum_significant_digits** | **int** |  | [optional] 
**as_boolean** | **bool** |  | [optional] 
**as_date** | **bool** |  | [optional] 
**as_slider** | **bool** |  | [optional] 
**resolution** | **float** |  | [optional] 
**date_style** | **str** |  | [optional] 
**time_style** | **str** |  | [optional] 
**day_period** | **str** |  | [optional] 
**hour12** | **bool** |  | [optional] 
**iso8601** | **bool** |  | [optional] 
**weekday** | **str** |  | [optional] 
**era** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**month** | **str** |  | [optional] 
**week** | **str** |  | [optional] 
**day** | **str** |  | [optional] 
**hour** | **str** |  | [optional] 
**minute** | **str** |  | [optional] 
**second** | **str** |  | [optional] 
**fractional_second_digits** | **int** |  | [optional] 
**time_zone_name** | **str** |  | [optional] 
**moment_js_format** | **str** |  | [optional] 
**as_number** | **bool** |  | [optional] 
**as_on_off** | **bool** |  | [optional] 
**as_pressed_released** | **bool** |  | [optional] 
**as_open_closed** | **bool** |  | [optional] 
**as_momentary** | **bool** |  | [optional] 
**multiline** | **bool** |  | [optional] 

## Example

```python
from or_rest_client.models.value_format import ValueFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFormat from a JSON string
value_format_instance = ValueFormat.from_json(json)
# print the JSON string representation of the object
print(ValueFormat.to_json())

# convert the object into a dict
value_format_dict = value_format_instance.to_dict()
# create an instance of ValueFormat from a dict
value_format_from_dict = ValueFormat.from_dict(value_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


