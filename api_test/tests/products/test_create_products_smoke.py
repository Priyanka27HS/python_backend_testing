from api_test.src.utilities.genericUtilities import generate_random_string
from api_test.src.helpers.products_helper import ProductsHelper
from api_test.src.dao.products_dao import ProductsDAO
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]

# Summary of this Test Case Id 26
# we created the product
# we generated a random name for the product
# we set the price and type and we made the API call
# we verified the status code is 201 bcz we specified that in helper class we say expected status is 201
# we got the response and made sure response is not empty, there is some data in response
# we made sure that the name in the response matches the name in the request and we got the ID from the response
# went to the db, got the product and compared the name and the product and the db, which is called post title is
# the same as the name in the request


# @pytest.mark.products
@pytest.mark.tcid26
def test_create_1_simple_product():
    # generate some data for the product
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the API call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product API response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product API call response has" \
                                                  f"Unexpected name. Expected : {payload['name']}, Actual : {product_rs['name']}"

    # verify the product exists in db
    # create an instance of the class and make the call

    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    # verify whether the info in the db matches the info thats in the call
    # in db name is going to be post title thats the name here
    # assert payload name is same as db product post title
    # list of dictionaries is here to get the first index of the list

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match " \
                                                           f"Title in API. DB: {db_product['post_title']}, API: {payload['name']}"
