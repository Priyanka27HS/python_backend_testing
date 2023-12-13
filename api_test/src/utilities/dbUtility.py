import pymysql
# import os
import logging as logger
from api_test.src.utilities.credentialsUtility import CredentialsUtility
# from api_test.src.configs.hosts_config import DB_HOST


# there few options to be able to work with mysql and python, the one we are using here is pyMySql
# when we run a query first we need a connection, so create a function to create a connection
# above both functions need to create a connection and any other new function also they need a new connection
# so create 1 method for create connection
# this is the utility for database

class DBUtility(object):

    # here you have set the environment
    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()

        self.host = 'localhost'
        self.socket = "/Users/testvagrant/Library/Application Support/Local/run/YJtkawwJ-/mysql/mysqld.sock"

        # self.machine = os.environ.get('MACHINE')
        # assert self.machine, f"Environment variable 'MACHINE' must be set."
        #
        # self.wp_host = os.environ.get('WP_HOST')
        # assert self.wp_host, f"Environment variable 'WP_HOST' must be set."
        #
        # if self.machine == 'docker' and self.wp_host == 'local':
        #     raise Exception(f"Cannot run tests in docker if WP_HOST='local")
        #
        # self.env = os.environ.get('ENV', 'test')
        #
        # self.host = DB_HOST[self.machine][self.env]['host']
        # self.socket = DB_HOST[self.machine][self.env]['socket']
        # self.port = DB_HOST[self.machine][self.env]['port']
        # self.database = DB_HOST[self.machine][self.env]['database']
        # self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):

        connection = pymysql.connect(host=self, user=self.creds['DB_USER'], password=self.creds['DB_PASSWORD'],
                                     unix_socket = self.socket)

        # if self.wp_host == 'local':
        #     connection = pymysql.connect(host=self, user=self.creds['DB_USER'], password=self.creds['DB_PASSWORD'],
        #                              unix_socket=self.socket)
        # elif self.wp_host == 'ampps':
        #     connection = pymysql.connect(host=self, user=self.creds['DB_USER'], password=self.creds['DB_PASSWORD'],
        #                              port=self.port)
        # else:
        #     raise Exception("Unknown WP_Host")

        return connection

    # function to run a query, execute and select queries
    def execute_select(self, sql):

        conn = self.create_connection()

        # we want to run a query we are going to get all the records in the database as a list of dictionaries each
        # row is going to be a dictionary and the key of each dictionary is going to be the heading of the column the
        # column heading will be a key and each row will be a dictionary and the whole thing you will get as list(
        # return type) fetchall - to get all the records

        try:
            logger.debug(f"Executing : {sql}")

            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql : {sql} \n Error : {str(e)}")
        finally:
            conn.close()

        return rs_dict

    # function to execute, update, delete, insert -> generic one
    def execute_sql(self, sql):
        pass
