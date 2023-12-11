import pytest
from api_test.src.utilities.requestsUtility import RequestsUtility
from api_test.src.dao.products_dao import ProductsDAO
from api_test.src.helpers.products_helper import ProductsHelper

# this tests should be tagged as smoke
# we can add it as module level
# instead of tagging each of the test cases product in smoke, we can add, we can tag the entire file with those tags

pytestmark = [pytest.mark.products, pytest.mark.smoke]

# for every test case you have to verify the status code
# you have to make sure that API is responding the right status code
# in our framework its lower level
# here prod id is 200 - status code


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get(endpoint='products')
    assert rs_api, f"Get all products end point returned nothing"


@pytest.mark.products
@pytest.mark.tcid25
def test_get_product_by_id():
    # get a product (test data) from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make the API call, rand_product_id - id we got from db
    product_helper = ProductsHelper()
    rest_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rest_api['name']

    # import pdb; pdb.set_trace()

    # in the API response there is a field called name and that name should match the post name in the database
    # so do assert for that verification
    # verify the response code - 200
    # data in the database is equals data in the API response
    assert db_name == api_name, f"Get product by ID returned wrong product. Id: {rand_product_id}" \
                                f"Db name :{db_name}, Api name: {api_name}"

    import pdb; pdb.set_trace()
