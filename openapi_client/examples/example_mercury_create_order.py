import os
from openapi_client.api import default_api
from openapi_client.examples.constants import ENV_NAME_CLIENT_ID, \
    ENV_NAME_CLIENT_SECRET, BASE_URL, ENV_NAME_X_API_KEY, ASSESSMENT_ID
from openapi_client.models.mercury_candidate import MercuryCandidate
from openapi_client.models.o_auth_request import OAuthRequest
from openapi_client.models.o_auth_response import OAuthResponse
from openapi_client.models.order_request import OrderRequest
from openapi_client.models.order_create_response import OrderCreateResponse
from openapi_client.configuration import Configuration
import openapi_client


def main():

    client_id = os.getenv(ENV_NAME_CLIENT_ID)
    client_secret = os.getenv(ENV_NAME_CLIENT_SECRET)

    configuration = Configuration(host=BASE_URL)
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        o_auth_request = OAuthRequest(
            client_id=client_id,
            client_secret=client_secret,
            grant_type="client_credentials"
        )
        try:
            oauth_response: OAuthResponse = api_instance.mercury_o_auth(
                o_auth_request=o_auth_request)

            x_api_key = os.getenv(ENV_NAME_X_API_KEY)
            auth = f"Bearer {oauth_response.access_token}"

            candidate = MercuryCandidate(
                email="test978@example.com",
                first_name="Test",
                last_name="Example",
                external_id="test978_example"
            )

            meta_data = {"job_name": "ceo"}
            order_request = OrderRequest(
                candidate=candidate,
                assessment_id=ASSESSMENT_ID,
                application_id="test_example_978",
                metadata=meta_data
            )

            create_order_response: OrderCreateResponse = api_instance.mercury_create_order(
                authorization=auth,
                x_api_key=x_api_key,
                order_request=order_request
            )

            print(f"Successfully created order: {create_order_response}")

        except openapi_client.ApiException as e:
            print(f"Exception when calling mercury api {e}")


if __name__ == '__main__':
    main()

