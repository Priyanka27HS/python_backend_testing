from api_test.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        # this give a bunch of 5000 rows and return random ones
        sql = 'SELECT * FROM local.wp_posts WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):

        sql = f"SELECT * FROM local.wp_posts WHERE id = {product_id};"

        return self.db_helper.execute_select(sql)

    def get_products_created_after_given_date(self, _date):

        sql = f'SELECT * FROM local.wp_posts where post_type = "product" AND post_date > "{_date}" LIMIT 10000;'

        return self.db_helper.execute_select(sql)