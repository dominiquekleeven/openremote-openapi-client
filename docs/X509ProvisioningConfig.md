# X509ProvisioningConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**X509ProvisioningData**](X509ProvisioningData.md) |  | [optional] 

## Example

```python
from openremote_openapi_client.models.x509_provisioning_config import X509ProvisioningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of X509ProvisioningConfig from a JSON string
x509_provisioning_config_instance = X509ProvisioningConfig.from_json(json)
# print the JSON string representation of the object
print(X509ProvisioningConfig.to_json())

# convert the object into a dict
x509_provisioning_config_dict = x509_provisioning_config_instance.to_dict()
# create an instance of X509ProvisioningConfig from a dict
x509_provisioning_config_from_dict = X509ProvisioningConfig.from_dict(x509_provisioning_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


