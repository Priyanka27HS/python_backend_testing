from api_test.src.utilities.requestsUtility import RequestsUtility


# import the RequestsUtility, we created a helper class and the actual method is to we need to call the API
# get the products by iD
class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")