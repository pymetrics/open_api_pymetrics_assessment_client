import os

import openapi_client
from openapi_client.api import default_api
from openapi_client.configuration import Configuration
from openapi_client.examples.constants import ENV_NAME_CLIENT_ID, \
    ENV_NAME_CLIENT_SECRET, BASE_URL
from openapi_client.models.o_auth_request import OAuthRequest
from openapi_client.models.o_auth_response import OAuthResponse


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

            print(f"Successfully retrieved token: {oauth_response.access_token}")

        except openapi_client.ApiException as e:
            print(f"Exception when calling mercury api {e}")


if __name__ == '__main__':
    main()

