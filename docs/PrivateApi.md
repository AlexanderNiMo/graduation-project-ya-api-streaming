# streaming_api.PrivateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_location_api_v1_add_file_location_post**](PrivateApi.md#add_file_location_api_v1_add_file_location_post) | **POST** /api/v1/add_file_location | Добавление информации о местонахождении файла

# **add_file_location_api_v1_add_file_location_post**
> Object add_file_location_api_v1_add_file_location_post(body)

Добавление информации о местонахождении файла

Добавление информации о местонахождении файла

### Example
```python
from __future__ import print_function
import time
import streaming_api
from streaming_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = streaming_api.PrivateApi()
body = streaming_api.MediaLocation() # MediaLocation | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.add_file_location_api_v1_add_file_location_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->add_file_location_api_v1_add_file_location_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaLocation**](MediaLocation.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

