import json
import os
from api_test.src.utilities.wooAPIUtility import WooAPIUtility
from api_test.src.dao.orders_dao import OrdersDao


# first get the path of the current file and get the path of the create_order_payload.json file path relative to this


class OrdersHelper(object):

    # how to get the current file path in python
    def __init__(self):
        self.curr_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args=None):

        # join will join all those strings based on the platform (Eg: Mac, Windows, Linux etc..)
        payload_template = os.path.join(self.curr_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more info to payload, then update it
        # additional_args is a dictionary and it exists
        # we upload the payload and need to make the API call
        # for the API call, we are going to use the woo-commerce API which we created in utilities
        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional_args' must be a dictionary but found {type(additional_args)}"
            payload.update(additional_args)

        rest_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)

        return rest_api

    @staticmethod
    def verify_order_is_created(order_json, exp_cust_id, exp_products):


        orders_dao = OrdersDao()

        # verify response
        assert order_json, f"Create order response is empty."

        assert order_json['customer_id'] == exp_cust_id, f"Create order with given customer id returned " \
                                                         f"Bad customer ID. Expected customer_id = {exp_cust_id} but got '{order_json['customer_id']}'"

        assert len(order_json['line_items']) == len(exp_products), f"Expected only {len(exp_products)} item in order but " \
                                                   f"Found '{len(order_json['line_items'])}' " \
                                                   f"Order id : {order_json['id']}"

        # verify database
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)

        assert line_info, f"Create order, line item not found in DB. Order Id: {order_id}"

        # verify line item and shipping and from the line_items we need to get the product id as well
        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']

        assert len(line_items) == 1, f"Expected 1 line item but found {len(line_items)}, Order id : {order_id}"

        # get list of product ids in the response
        api_products_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_products_ids, f"Create order does not have at least 1 expected product in DB."\
                                                              f"Product Id: {product['product_id']}. Order Id : {order_id}  "

