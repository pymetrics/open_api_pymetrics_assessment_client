# pymetrics_soft_skills_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mercury_create_order_v2**](DefaultApi.md#mercury_create_order_v2) | **POST** /mercury/v2/orders | Create Assessment Order
[**mercury_get_config_v2**](DefaultApi.md#mercury_get_config_v2) | **GET** /mercury/v2/assessments | Get Assessment Configurations
[**mercury_list_orders_v2**](DefaultApi.md#mercury_list_orders_v2) | **GET** /mercury/v2/orders | List Assessment Orders
[**mercury_o_auth_v2**](DefaultApi.md#mercury_o_auth_v2) | **POST** /mercury/v2/oauth/token | Generate OAuth Token
[**mercury_retrieve_factor_content**](DefaultApi.md#mercury_retrieve_factor_content) | **GET** /mercury/v2/factorContent/{uuid} | Get Factor Content
[**mercury_retrieve_order_v2**](DefaultApi.md#mercury_retrieve_order_v2) | **GET** /mercury/v2/orders/{uuid} | Get Assessment Order


# **mercury_create_order_v2**
> OrderCreateResponse mercury_create_order_v2(authorization=authorization, x_api_key=x_api_key, order_request=order_request)

Create Assessment Order

Creates an assessment order for a candidate. This represents the transaction for a candidate's job application.  This is an idempotent operation, and may return an existing assessment order. The following inputs constitute the uniqueness criteria: * `candidate.email` * `assessment_id` * `application_id` 

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)
order_request = pymetrics_soft_skills_sdk.OrderRequest() # OrderRequest | Candidate, assessment, and job application details (optional)

    try:
        # Create Assessment Order
        api_response = api_instance.mercury_create_order_v2(authorization=authorization, x_api_key=x_api_key, order_request=order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_create_order_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Standard Bearer token request, from &#x60;Generate OAuth Token&#x60;. Formatted &#x60;Bearer {token}&#x60; | [optional] 
 **x_api_key** | **str**| Mandatory API Key that pymetrics will provide | [optional] 
 **order_request** | [**OrderRequest**](OrderRequest.md)| Candidate, assessment, and job application details | [optional] 

### Return type

[**OrderCreateResponse**](OrderCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found an existing assessment order with the same candidate.email, assessment_id, and application_id |  -  |
**201** | Created a new assessment order |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid OAuth credentials |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mercury_get_config_v2**
> Configuration mercury_get_config_v2(authorization=authorization, x_api_key=x_api_key)

Get Assessment Configurations

Lists the assessment templates that are currently registered for your integration. These are configured outside of the API, and represent the different candidate experiences for each role pymetrics is being leveraged for. 

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)

    try:
        # Get Assessment Configurations
        api_response = api_instance.mercury_get_config_v2(authorization=authorization, x_api_key=x_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_get_config_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Standard Bearer token request, from &#x60;Generate OAuth Token&#x60;. Formatted &#x60;Bearer {token}&#x60; | [optional] 
 **x_api_key** | **str**| Mandatory API Key that pymetrics will provide | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available configurations |  -  |
**401** | Invalid OAuth credentials |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mercury_list_orders_v2**
> ListOrdersResponse mercury_list_orders_v2(job_application_id=job_application_id, candidate_id=candidate_id, authorization=authorization, x_api_key=x_api_key)

List Assessment Orders

Get a list of Assessment Orders by either job application ID and/or candidate ID. At least one of the IDs must be provided.

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    job_application_id = 'job_application_id_example' # str | Job application ID by which to optionally filter on (optional)
candidate_id = 'candidate_id_example' # str | Candidate ID by which to optionally filter on (optional)
authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)

    try:
        # List Assessment Orders
        api_response = api_instance.mercury_list_orders_v2(job_application_id=job_application_id, candidate_id=candidate_id, authorization=authorization, x_api_key=x_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_list_orders_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_application_id** | **str**| Job application ID by which to optionally filter on | [optional] 
 **candidate_id** | **str**| Candidate ID by which to optionally filter on | [optional] 
 **authorization** | **str**| Standard Bearer token request, from &#x60;Generate OAuth Token&#x60;. Formatted &#x60;Bearer {token}&#x60; | [optional] 
 **x_api_key** | **str**| Mandatory API Key that pymetrics will provide | [optional] 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of orders, if any were found, for the supplied IDs |  -  |
**400** | Neither a job application ID nor a candidate ID were provided |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mercury_o_auth_v2**
> OAuthResponse mercury_o_auth_v2(o_auth_request=o_auth_request)

Generate OAuth Token

The response's bearer token must be used in the `Authorization` header for any other API request. Tokens are valid for only a period of time.  All requests, with the exception of this one, also require an API Key to be supplied in the `X-Api-Key` request header. pymetrics will supply this along with the OAuth Client ID and Secret. 

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    o_auth_request = pymetrics_soft_skills_sdk.OAuthRequest() # OAuthRequest | OAuth2 Client Credentials (optional)

    try:
        # Generate OAuth Token
        api_response = api_instance.mercury_o_auth_v2(o_auth_request=o_auth_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_o_auth_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_request** | [**OAuthRequest**](OAuthRequest.md)| OAuth2 Client Credentials | [optional] 

### Return type

[**OAuthResponse**](OAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OAuth Bearer Token |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid OAuth credentials |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mercury_retrieve_factor_content**
> MercuryOrderFactorContent mercury_retrieve_factor_content(uuid, authorization=authorization, x_api_key=x_api_key)

Get Factor Content

Gets the factor content for an assessment order by its ID.

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    uuid = 'uuid_example' # str | The Order ID value from creating the order.
authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)

    try:
        # Get Factor Content
        api_response = api_instance.mercury_retrieve_factor_content(uuid, authorization=authorization, x_api_key=x_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_retrieve_factor_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The Order ID value from creating the order. | 
 **authorization** | **str**| Standard Bearer token request, from &#x60;Generate OAuth Token&#x60;. Formatted &#x60;Bearer {token}&#x60; | [optional] 
 **x_api_key** | **str**| Mandatory API Key that pymetrics will provide | [optional] 

### Return type

[**MercuryOrderFactorContent**](MercuryOrderFactorContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Factor content for the requested order |  -  |
**400** | Could not retrieve factor scores for order |  -  |
**404** | Order ID not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mercury_retrieve_order_v2**
> MercuryAssessmentOrder mercury_retrieve_order_v2(uuid, report=report, authorization=authorization, x_api_key=x_api_key)

Get Assessment Order

Get an existing order by ID. It will move from `Completed` to `Fulfilled` if the order has results.

### Example

```python
from __future__ import print_function
import time
import pymetrics_soft_skills_sdk
from pymetrics_soft_skills_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetrics_soft_skills_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymetrics_soft_skills_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pymetrics_soft_skills_sdk.DefaultApi(api_client)
    uuid = 'uuid_example' # str | The Order ID value from creating the order. The create operation is idempotent, based on candidate.email, assessment_id, and application_id
report = True # bool | Set to true to optionally force a report to be generated if one does not exist (optional)
authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)

    try:
        # Get Assessment Order
        api_response = api_instance.mercury_retrieve_order_v2(uuid, report=report, authorization=authorization, x_api_key=x_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_retrieve_order_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The Order ID value from creating the order. The create operation is idempotent, based on candidate.email, assessment_id, and application_id | 
 **report** | **bool**| Set to true to optionally force a report to be generated if one does not exist | [optional] 
 **authorization** | **str**| Standard Bearer token request, from &#x60;Generate OAuth Token&#x60;. Formatted &#x60;Bearer {token}&#x60; | [optional] 
 **x_api_key** | **str**| Mandatory API Key that pymetrics will provide | [optional] 

### Return type

[**MercuryAssessmentOrder**](MercuryAssessmentOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found an existing assessment order for the supplied ID |  -  |
**404** | Order ID not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

