from api_test.src.utilities.dbUtility import DBUtility


class OrdersDao(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_lines_by_order_id(self, order_id):

        # in sql pass order id
        sql = f'SELECT * FROM local.wp_woocommerce_order_items where order_id = {order_id};'

        return self.db_helper.execute_select(sql)

    # another function to get the metadata per for order line
    def get_order_items_details(self, order_item_id):

        sql = f"SELECT * FROM local.wp_woocommerce_order_itemmeta WHERE order_item_id = {order_item_id};"
        rs_sql = self.db_helper.execute_select(sql)

        # create a dictionary for each n every row
        # we are looping through each row to get key and value pair
        line_details = dict()
        for meta in rs_sql:
            line_details[meta['meta_key']] = meta['meta_value']

        return line_details

        import pdb; pdb.set_trace()