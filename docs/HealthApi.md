# streaming_api.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_streaming_api_api_health_check_get**](HealthApi.md#health_check_streaming_api_api_health_check_get) | **GET** /streaming_api/api/health/check/ | Health Check

# **health_check_streaming_api_api_health_check_get**
> Object health_check_streaming_api_api_health_check_get()

Health Check

### Example
```python
from __future__ import print_function
import time
import streaming_api
from streaming_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = streaming_api.HealthApi()

try:
    # Health Check
    api_response = api_instance.health_check_streaming_api_api_health_check_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_check_streaming_api_api_health_check_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

