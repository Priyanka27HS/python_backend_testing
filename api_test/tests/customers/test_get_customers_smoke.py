# we imported the helper -> RequestsUtility
# we created an object of the helper RequestsUtility
# we made a GET call API

import pytest
from api_test.src.utilities.requestsUtility import RequestsUtility
import logging as logger


# make the API call to get call to customers
@pytest.mark.customers
@pytest.mark.sample_tc
def test_get_all_customers():
    # create an object for requests helper
    req_helper = RequestsUtility()

    # make a GET call API
    rest_api = req_helper.get('customers')
    # logger.debug(f"Response of list all : {rest_api}")

    assert rest_api, f"Response of list all customers is empty"

    # import pdb; pdb.set_trace()
