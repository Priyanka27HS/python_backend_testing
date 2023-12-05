from api_test.src.utilities.dbUtility import DBUtility
import random

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    # limit is set as 5000 here so qty shouldnt be more than it
    def get_random_customer_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_posts ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        # return type is list
        return random.sample(rs_sql, int(qty))
