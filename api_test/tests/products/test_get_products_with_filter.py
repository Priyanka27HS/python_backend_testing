import pytest
from datetime import datetime, timedelta
import pdb
from api_test.src.helpers.products_helper import ProductsHelper
from api_test.src.dao.products_dao import ProductsDAO


# test class shouldn't have an init constructor @pytest.mark.tcid51 this going to have bunch of test cases,
# each one has an ID, but everything is a regression so whatever you apply to the class name automatically gets
# inherited by the method names / by the tests this test is going to run today, next month, next year,
# etc.. ->  x_days_from_today = 30 this is going to give me all products created in the last 30 days ->
# x_days_from_today = 30 you can change the number of this  x_days_from_today = 30 or empty as well we created the
# payload, added a filter we figured out a data and used in the code and made the API call go to the database,
# get use SQL to get all products created after the same exact date and then compare 2 results only way we know the
# test case returned, the correct number of the correct no of products is by actually checking the database to make
# sure the no of products in the database is the same as what the API returned we need to compare is the no of
# products returned with the API is the same as the number of products returned in the database


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        # create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # temp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = temp_date.strftime('%Y-%M-%dT%H:%m:%S')

        payload = dict()
        payload['after'] = after_created_date
        payload['per_page'] = 100
        # payload['after'] = datetime.now() - timedelta(days=x_days_from_today)

        # make the API call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response for list of products with filter"

        # get data from the db
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # verify response matches db
        assert len(rs_api) == len(db_products), f"List products with filter 'after' returned unexpected number of products." \
                                                f"Expected: {len(db_products)}, Actual: {len(rs_api)}"

        # get all the ID's in the db and get all the ID's in the API and jus make sure that they all are same
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        # compare the above 2 lists are same
        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f"List products with filter, product ids in response mismatch in db."
