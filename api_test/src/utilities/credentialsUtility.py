import os
import subprocess

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
from dotenv import load_dotenv


class CredentialsUtility(object):

    def __init__(self):
        pass

    # we don't have to instantiate an object/create a object so we use static method
    @staticmethod
    def get_wc_api_keys():

        load_dotenv("/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh")
        subprocess.run(
            'source "/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh"',
            shell=True)

        # to get the environments
        os.system("source env.sh")

        wc_key = os.environ.get("WC_KEY")
        wc_secret = os.environ.get("WC_SECRET")

        print("WC_KEY:", wc_key)
        print("WC_SECRET:", wc_secret)

        # print(os.environ.get("WC_Key"))
        # print(os.environ.get("WC_Secret"))

        if not wc_key or not wc_secret:
            raise Exception("The API credentials for 'WC_Key' and 'WC_Secret' must be in environment variables")
        else:
            return {"WC_KEY": wc_key, "WC_SECRET": wc_secret}

    # method to get database credentials and use environment variables here
    # getting info from the database and then validating the information is set and returning it
    # we need a helper method to get our credentials from the environment
    # helper class added for db and added our credentials
    @staticmethod
    def get_db_credentials():

        load_dotenv("/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh")
        subprocess.run(
            'source "/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh"',
            shell=True)

        os.system("source env.sh")

        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

        print("DB_USER:", db_user)
        print("DB_PASSWORD:", db_password)

        if not db_user or not db_password:
            raise Exception("The DB credentials for 'DB_USER' and 'DB_PASSWORD' must be in environment variables")
        else:
            return {"DB_USER": db_user, "DB_PASSWORD": db_password}
