from api_test.src.utilities.genericUtilities import generate_random_email_and_password
from api_test.src.utilities.requestsUtility import RequestsUtility

# here we jus wrote the code that calls the function to generate email and jus creates the payload
# and we didn't make the call
# now we are going to implement the part that we actually making the call
# we need a helper class that we jus specify the url and the payload and it makes a call for us
# This is typical in any framework


class CustomerHelper(object):

    def __init__(self):
        print('Creating object')
        self.requests_utility = RequestsUtility()
        print('Object created')

    # create a main function -> create customer, make as keyword args so that the user can pass whatever data
    # kwargs -> very neat feature for python, kwargs is a dictionary you can pass whatever needed as dictionary
    # here we have dictionary as payload, and we are jus going to update it
    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        # make the post api call here
        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)

        # return json response here
        return create_user_json

# woo-commerce provides us python library
# pip install Woocommerce
