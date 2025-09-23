# AssetTreeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**AssetObject**](AssetObject.md) |  | [optional] 
**children** | [**List[AssetTreeNode]**](AssetTreeNode.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.asset_tree_node import AssetTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTreeNode from a JSON string
asset_tree_node_instance = AssetTreeNode.from_json(json)
# print the JSON string representation of the object
print(AssetTreeNode.to_json())

# convert the object into a dict
asset_tree_node_dict = asset_tree_node_instance.to_dict()
# create an instance of AssetTreeNode from a dict
asset_tree_node_from_dict = AssetTreeNode.from_dict(asset_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


