from api_test.src.utilities.requestsUtility import RequestsUtility
import logging as logger


# import the RequestsUtility, we created a helper class and the actual method is to we need to call the API
# get the products by iD
class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)

    # filter is part of payload -> it can be used in any tests, its none and we couldnt call it without a filter
    # and it returns all of the products
    def call_list_products(self, payload=None):

        # we are going to call the method and if they are in the response, if there in any data then we are going to
        # call it again and again until we get an empty response
        # if we get an empty response we are in the end of the available data

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number : {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 3

            # add the current page number to the call
            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload=payload)

        # if there is not response then stop the loop bcz there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products
