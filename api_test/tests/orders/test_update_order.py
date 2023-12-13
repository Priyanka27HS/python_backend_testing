from api_test.src.helpers.orders_helper import OrdersHelper
from api_test.src.utilities.wooAPIUtility import WooAPIUtility
import pytest
from api_test.src.utilities.genericUtilities import generate_random_string

pytestmark = [pytest.mark.orders, pytest.mark.regression]


# the same parameter should be passed in the first argument in the parameter
@pytest.mark.parametrize("new_status",
                         [
                             pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                             pytest.param('completed', marks=pytest.mark.tcid56),
                             pytest.param('on-hold', marks=pytest.mark.tcid57),
                         ])
def test_update_order_status(new_status):
    # new_status = 'cancelled'
    # new_status = 'completed'

    # create new order and get the current status of the order
    order_helper = OrdersHelper()
    order_json = OrdersHelper().create_order()
    current_status = order_json['status']

    assert current_status != new_status, f"Current status of order is already {new_status}. " \
                                         f"Unable to run test."

    # update the status and payload -> valid one
    order_id = order_json['id']
    payload = {"status": new_status}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status}'," \
                                                   f"but order is still '{new_order_info['status']}'"


@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    # new status for random string
    new_status = 'abcdefgh'

    # create new order
    order_helper = OrdersHelper()
    order_json = OrdersHelper().create_order()
    order_id = order_json['id']

    # update the order with new status
    # instead of calling the helper class we just call the PUT Api directly and the WooCommerce API library
    # passed the payload and expected status code 400
    # PUT will automatically validate the expected status code
    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)

    # give this cmd -> pp rs_api
    # code, data and message are give in the response, so we are validating those 3

    assert rs_api['code'] == 'rest_invalid_param', f"Update order status to random string did not have " \
                                                   f"Correct code in response. Expected 'rest_invalid_param' Actual : {rs_api['code']}"

    assert rs_api['message'] == 'Invalid parameter(s): status', f"Update order status to random " \
                                                                f"String did not have correct message in response. " \
                                                                f"Expected : 'rest_invalid_param' Actual : {rs_api['message']}"


# we updated the customer note of the order
@pytest.mark.tcid59
def test_update_order_customer_note():

    # we created the helper class
    # we made the call to create new order
    # create order takes payload from a JSON file
    order_helper = OrdersHelper()
    order_json = OrdersHelper().create_order()
    order_id = order_json['id']

    # update the status
    # we are testing only 1 field that's the customer note and verify it
    rand_string = generate_random_string(40)
    payload = {"customer_note": rand_string}
    order_helper.call_update_an_order(order_id, payload)

    # get order information, make another API call
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    assert new_order_info['customer_note'] == rand_string, f"Update order's 'customer_note' field failed." \
                                                           f"Expected : {rand_string}, Actual : {new_order_info['customer_note']}"
