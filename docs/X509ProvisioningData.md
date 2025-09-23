# X509ProvisioningData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_pem** | **str** |  | [optional] 
**ignore_expiry_date** | **bool** |  | [optional] 

## Example

```python
from openremote_openapi_client.models.x509_provisioning_data import X509ProvisioningData

# TODO update the JSON string below
json = "{}"
# create an instance of X509ProvisioningData from a JSON string
x509_provisioning_data_instance = X509ProvisioningData.from_json(json)
# print the JSON string representation of the object
print(X509ProvisioningData.to_json())

# convert the object into a dict
x509_provisioning_data_dict = x509_provisioning_data_instance.to_dict()
# create an instance of X509ProvisioningData from a dict
x509_provisioning_data_from_dict = X509ProvisioningData.from_dict(x509_provisioning_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


