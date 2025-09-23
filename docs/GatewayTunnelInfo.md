# GatewayTunnelInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm** | **str** |  | [optional] 
**gateway_id** | **str** |  | [optional] 
**target_port** | **int** |  | [optional] 
**target** | **str** |  | [optional] 
**assigned_port** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**auto_close_time** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.gateway_tunnel_info import GatewayTunnelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayTunnelInfo from a JSON string
gateway_tunnel_info_instance = GatewayTunnelInfo.from_json(json)
# print the JSON string representation of the object
print(GatewayTunnelInfo.to_json())

# convert the object into a dict
gateway_tunnel_info_dict = gateway_tunnel_info_instance.to_dict()
# create an instance of GatewayTunnelInfo from a dict
gateway_tunnel_info_from_dict = GatewayTunnelInfo.from_dict(gateway_tunnel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


