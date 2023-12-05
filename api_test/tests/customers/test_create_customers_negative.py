import pytest

from api_test.src.dao.customers_dao import CustomersDAO
from api_test.src.helpers.customers_helper import CustomerHelper
from api_test.src.utilities.genericUtilities import generate_random_email_and_password
from api_test.src.utilities.requestsUtility import RequestsUtility
import logging as logger


# make a call to create customer
# make sure that users cannot create a accounts with an existing email
# write a function now that is going to the database and get an existing user
# made the api call and validating, and we also validating the status code
# we made the api call with that email address from the database hard coded password
# and we passed in the expected status code to be a 400
# we know we are getting an error and the error has a code and a message and we validated those two by hard coding what

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    # get existing email from the database
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    # existing_email = existing_cust[0]['user_email']
    existing_email = existing_cust[0].get('user_email')

    # call the api
    req_helper = RequestsUtility()

    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert (cust_api_info['code'] == 'rest_missing_callback_param'), (
        f"Create customer with "
        f"Existing user error 'code' is not correct. "
        f"Expected 'rest_missing_callback_param', "
        f"Actual : {cust_api_info['code']}"
    )

    assert (cust_api_info['message'] == 'Missing parameter(s): email'), (
        f"Create customer with existing user error 'message' is not correct. "
        f"Expected 'Missing parameter(s): email', "
        f"Actual : {cust_api_info['message']}"
    )

    # Given in course :
    # assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with" \
    # f"Existing user error 'code' is not correct. Expected 'registration-error-email-exists', " \
    # f"Actual : {cust_api_info['code']}"

    # assert cust_api_info['message'] == 'An account is already registrated with your email address. Please log in', \
    #   f"Create customer with existing user error 'message' is not correct. " \
    #   f"Expected 'An account is already registrated with your email address. Please log in', " \
    #   f"Actual : {cust_api_info['message']}"

    # import pdb; pdb.set_trace()
