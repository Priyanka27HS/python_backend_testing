import logging as logger
import subprocess
import os

def test_health_check1():
    logger.info("Running health check test1")


    # Execute the shell script to set environment variables
    # subprocess.run("/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh", shell=True)


    # Access the environment variables in Python
    wc_key = os.environ.get("WC_KEY")
    wc_secret = os.environ.get("WC_SECRET")

    # Now, you can use wc_key and wc_secret in your test
    print("WC_KEY:", wc_key)
    print("WC_SECRET:", wc_secret)

