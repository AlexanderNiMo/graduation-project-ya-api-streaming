# streaming_api.FileLocationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_location_api_v1_add_file_location_post**](FileLocationApi.md#add_file_location_api_v1_add_file_location_post) | **POST** /api/v1/add_file_location | Добавление информации о местонахождении файла
[**get_streaming_url_streaming_api_api_v1_get_streaming_url_post**](FileLocationApi.md#get_streaming_url_streaming_api_api_v1_get_streaming_url_post) | **POST** /streaming_api/api/v1/get_streaming_url | Добавление информации о местонахождении файла

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
api_instance = streaming_api.FileLocationApi()
body = streaming_api.MediaLocation() # MediaLocation | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.add_file_location_api_v1_add_file_location_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLocationApi->add_file_location_api_v1_add_file_location_post: %s\n" % e)
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

# **get_streaming_url_streaming_api_api_v1_get_streaming_url_post**
> Object get_streaming_url_streaming_api_api_v1_get_streaming_url_post(media_id, jwt_token=jwt_token, x_real_ip=x_real_ip)

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
api_instance = streaming_api.FileLocationApi()
media_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
jwt_token = 'jwt_token_example' # str |  (optional)
x_real_ip = 'x_real_ip_example' # str |  (optional)

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.get_streaming_url_streaming_api_api_v1_get_streaming_url_post(media_id, jwt_token=jwt_token, x_real_ip=x_real_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLocationApi->get_streaming_url_streaming_api_api_v1_get_streaming_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | [**str**](.md)|  | 
 **jwt_token** | **str**|  | [optional] 
 **x_real_ip** | **str**|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

