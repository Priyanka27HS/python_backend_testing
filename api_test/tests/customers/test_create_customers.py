import subprocess
import pytest
import logging as logger
import os
from dotenv import load_dotenv
from api_test.src.utilities.genericUtilities import generate_random_email_and_password
from api_test.src.helpers.customers_helper import CustomerHelper
from api_test.src.dao.customers_dao import CustomersDAO


# create a customer with jus basic info like email and password
# we wrote a helper function that will generate a random email and random password
# we also created a function that will create a customer basically thats going to take a parameters
# and then make api the call

@pytest.mark.customers
@pytest.mark.sample_tc
def test_create_customer_details():
    # here it auto generates random email each n every time the test run so we can create a helper class
    # that actually generates email addresses so we can use it in other tests

    logger.info("API Test - Create new customer with email and password")
    logger.debug("API Test - Create new customer with email and password")

    rand_info = generate_random_email_and_password()
    logger.info("Generating random email and password", rand_info)

    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # to make the api call - create helper class
    cust_obj = CustomerHelper()

    # call the function to create the customer
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # import pdb; pdb.set_trace()


    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer API return wrong email. Email{email}"
    assert cust_api_info['first_name'] == '', f"Create customer API returned value for first_name" (f"but it should be "
                                                                                                    f"empty")
    # get the user from database, create DAO
    # validate it
    # when we run sql itself is from the email

    # verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database. '\
                                  f'Email : {email}'

    # import pdb; pdb.set_trace()
