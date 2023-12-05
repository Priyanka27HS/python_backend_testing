import requests
from api_test.src.configs.hosts_config import API_HOSTS
from api_test.src.utilities.credentialsUtility import CredentialsUtility
import os
import json
import requests
from requests_oauthlib import OAuth1
import logging as logger


# function to make the api call

class RequestsUtility(object):

    def __init__(self):
        # jus call the method as such since it's a static method, no need to create an object for it
        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        self.auth = OAuth1(wc_creds["WC_KEY"], wc_creds["WC_SECRET"])

        # self.auth = OAuth1("ck_ab7ffe77766dc6872232cb548a467582f7cca6d9",
        #                    "cs_2e6106999cecc3ab913fc1609feb2fec11a431fa")

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code" \
                                                              f"Expected {self.expected_status_code}, Actual status code : {self.status_code}," \
                                                              f"URL : {self.url}, Response Json: {self.rs_json}"

    # we need a function for post api call
    # post will make a call and verifies the status code is the expected status codr
    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rest_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rest_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rest_api.json()
        self.assert_status_code()

        # assert self.status_code == int(expected_status_code), \
        #     f'Expected status code {expected_status_code} but actual {self.status_code}'

        logger.debug(f"POST API response : {rest_api.json()}")

        # returns the json response
        return self.rs_json

    # GET call API, they dont take payloads but sometimes they do
    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rest_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rest_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rest_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response : {rest_api.json()}")

        return self.rs_json

    # Update
    def update(self):
        pass

    # Delete
    def delete(self):
        pass
