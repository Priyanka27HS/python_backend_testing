import logging as logger
from api_test.src.configs.hosts_config import WOO_API_HOSTS
from api_test.src.utilities.credentialsUtility import CredentialsUtility
import os
from woocommerce import API


class WooAPIUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]

        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['WC_KEY'],
            consumer_secret=wc_creds['WC_SECRET'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code" \
                                                              f"Expected {self.expected_status_code}, Actual status code : {self.status_code}," \
                                                              f"URL : {self.endpoint}, Response Json: {self.rs_json}"

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rest_api = self.wcapi.post(wc_endpoint, data=params)
        self.status_code = rest_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rest_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"POST API response : {rest_api.json()}")

        return self.rs_json

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        rest_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rest_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rest_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"GET API response : {rest_api.json()}")

        return self.rs_json

    def put(self, wc_endpoint, params=None, expected_status_code=200):

        import pdb; pdb.set_trace()

        rest_api = self.wcapi.put(wc_endpoint, data=params)
        self.status_code = rest_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rest_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"PUT API response : {rest_api.json()}")

        return self.rs_json


# when the script is executed, if the script is invoked directly, this block will be executed
# this variable __name__, is a global variable thats going to be available is going to be set as main
if __name__ == '__main__':
    obj = WooAPIUtility()
    rest_api = obj.get('products')
    print(rest_api)

    import pdb; pdb.set_trace()
