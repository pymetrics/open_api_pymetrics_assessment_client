import os

import openapi_client
from openapi_client import ListOrdersRequest, ListOrdersResponse
from openapi_client.api import default_api
from openapi_client.configuration import Configuration
from openapi_client.examples.constants import ENV_NAME_CLIENT_ID, \
    ENV_NAME_CLIENT_SECRET, BASE_URL, ENV_NAME_X_API_KEY, CANDIDATE_ID, \
    JOB_APPLICATION_ID
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

            x_api_key = os.getenv(ENV_NAME_X_API_KEY)
            auth = f"Bearer {oauth_response.access_token}"



            list_orders_request_for_cand = ListOrdersRequest(
                candidate_id= CANDIDATE_ID
            )

            list_orders_response_for_cand: ListOrdersResponse = api_instance.mercury_list_orders(
                authorization=auth,
                x_api_key=x_api_key,
                list_orders_request=list_orders_request_for_cand
            )

            print(f"Successfully list order for candidate: {list_orders_response_for_cand}")

            list_orders_request_for_job_app = ListOrdersRequest(
                job_application_id=JOB_APPLICATION_ID
            )

            list_orders_response_for_job_app: ListOrdersResponse = \
                api_instance.mercury_list_orders(
                authorization=auth,
                x_api_key=x_api_key,
                list_orders_request=list_orders_request_for_job_app
            )

            print(
                f"Successfully list order for job app: {list_orders_response_for_job_app}")

        except openapi_client.ApiException as e:
            print(f"Exception when calling mercury api {e}")


if __name__ == '__main__':
    main()

