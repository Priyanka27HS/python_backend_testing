import pytest
from api_test.src.dao.products_dao import ProductsDAO
from api_test.src.helpers.orders_helper import OrdersHelper
from api_test.src.helpers.customers_helper import CustomerHelper


# we have some helper objects
# we got some random objects from the database and we call the create order
# create order is a new function we wrote in the helper and create order will
# read the template for the payload from a file
# so we created a json file that has the payload, so create order reads that file and it also takes a
# parameter for additional args
# so whatever user is done at additional args we pass that as payload

@pytest.fixture(scope='module')
def my_orders_smoke_setup():
    # create a helper class here
    product_dao = ProductsDAO()

    # get a random product from the db
    rand_product = product_dao.get_random_product_from_db()
    product_id = rand_product[0]['ID']

    # create a helper class here
    order_helper = OrdersHelper()

    info = {'product_id': product_id,
            'order_helper': order_helper}

    return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):

    order_helper = my_orders_smoke_setup['order_helper']

    customer_id = 0
    product_id = my_orders_smoke_setup['product_id']

    # make the API call -> it should be POST call and we should have a helper to make the call
    # product_id is got from database

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 2
        }
    ]}

    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    # create helper objects

    order_helper = my_orders_smoke_setup['order_helper']
    customer_helper = CustomerHelper()

    # make the API call -> it should be POST call and we should have a helper to make the call
    # add customer id
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    product_id = my_orders_smoke_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 2
        }
    ],
        "customer_id": customer_id
    }

    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
