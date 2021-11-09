# python-pymetrics-assessment-client
### This is pymetrics's public API for assessments, usually as part of a job application workflow.
The typical use case for this is to support an externally initiated assessment for a candidate job application.
This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application.

The expected sequence of API calls is:
* `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided
* `Get Assessment Configurations` to determine which configured assessment templates are available
* `Create Assessment Order` for a selected Assessment and candidate job application
* `Get Assessment Order` to receive the recommendation results, once they are available

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install


```sh
pip install python-pymetrics-assessment-client
```



## Usage

A full set of examples can be found in the [python_pymetrics_assessments_client examples directory](https://github.com/pymetrics/python_pymetrics_assessment_client/tree/main/openapi_client/examples).

To get started, please request Client ID, Client Secret and API Key from pymetrics.

Here is an example of retrieving an OAuth token and create an assessment order:

```python
from openapi_client.api import default_api
from openapi_client.models.mercury_candidate import MercuryCandidate
from openapi_client.models.o_auth_request import OAuthRequest
from openapi_client.models.o_auth_response import OAuthResponse
from openapi_client.models.order_request import OrderRequest
from openapi_client.models.order_create_response import OrderCreateResponse
from openapi_client.configuration import Configuration
import openapi_client

    client_id = INSERT_YOUR_CLIENT_ID_HERE
    client_secret = INSERT_YOUR_CLIENT_SECRET_HERE

    configuration = Configuration(host="https://staging.api.pymetrics.com")
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = default_api.DefaultApi(api_client)
        # Get an access token by hitting auth endpiont
        o_auth_request = OAuthRequest(
            client_id=client_id,
            client_secret=client_secret,
            grant_type="client_credentials"
        )
        try:
            oauth_response: OAuthResponse = api_instance.mercury_o_auth(
                o_auth_request=o_auth_request)

            x_api_key = INSERT_YOUR_API_KEY_HERE
            
            # pass this as authorization to any Mercury endpoint
            auth = f"Bearer {oauth_response.access_token}"
            
            # construct Create Assessment Order Request
            candidate = MercuryCandidate(
                email="test978@example.com",
                first_name="Test",
                last_name="Example",
                external_id="test978_example"
            )

            meta_data = {"job_name": "ceo"}
            order_request = OrderRequest(
                candidate=candidate,
                assessment_id=INSERT_YOUR_ASSESSMENT_ID_HERE,
                application_id="test_example_978",
                metadata=meta_data
            )
            
            # create an assessment order by hitting create order endpoint
            create_order_response: OrderCreateResponse = api_instance.mercury_create_order(
                authorization=auth,
                x_api_key=x_api_key,
                order_request=order_request
            )

            print(f"Successfully created order: {create_order_response}")

        except openapi_client.ApiException as e:
            # catch any exception incurred by api endpoinnts
            print(f"Exception when calling mercury api {e}")
```

## Documentation for API Endpoints

All URIs are relative to *http://staging.api.pymetrics.com* or *http://api.pymetrics.com* 

To access links below, please refer to README in [Documentation for API Endpoints](https://github.com/pymetrics/python_pymetrics_assessment_client/#documentation-for-api-endpoints)

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**mercury_create_order**](docs/DefaultApi.md#mercury_create_order) | **POST** /mercury/order | Create Assessment Order
*DefaultApi* | [**mercury_get_config**](docs/DefaultApi.md#mercury_get_config) | **GET** /mercury/configuration | Get Assessment Configurations
*DefaultApi* | [**mercury_list_orders**](docs/DefaultApi.md#mercury_list_orders) | **POST** /mercury/orders | List Assessment Orders
*DefaultApi* | [**mercury_o_auth**](docs/DefaultApi.md#mercury_o_auth) | **POST** /mercury/oauth/token | Generate OAuth Token
*DefaultApi* | [**mercury_retrieve_order**](docs/DefaultApi.md#mercury_retrieve_order) | **GET** /mercury/getOrder/{uuid} | Get Assessment Order


## Documentation For Models
To access links below, please refer to README in [Documentation for Models](https://github.com/pymetrics/python_pymetrics_assessment_client/#documentation-for-models)

 - [AssessmentType](docs/AssessmentType.md)
 - [AtsType](docs/AtsType.md)
 - [Configuration](docs/Configuration.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ListOrdersRequest](docs/ListOrdersRequest.md)
 - [ListOrdersResponse](docs/ListOrdersResponse.md)
 - [MercuryAssessment](docs/MercuryAssessment.md)
 - [MercuryAssessmentOrder](docs/MercuryAssessmentOrder.md)
 - [MercuryCandidate](docs/MercuryCandidate.md)
 - [MercuryReport](docs/MercuryReport.md)
 - [MercuryResult](docs/MercuryResult.md)
 - [OAuthRequest](docs/OAuthRequest.md)
 - [OAuthResponse](docs/OAuthResponse.md)
 - [OrderCreateResponse](docs/OrderCreateResponse.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [PontemOrderStatuses](docs/PontemOrderStatuses.md)



