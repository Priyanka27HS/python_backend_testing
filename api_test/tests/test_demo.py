# import subprocess
# import os
#
# # Execute the shell script to set environment variables
# subprocess.run("source env.sh", shell=True)
#
# # Access the environment variables in Python
# wc_key = os.environ.get("WC_KEY")
# wc_secret = os.environ.get("WC_SECRET")
#
# # Now, you can use wc_key and wc_secret in your test
# print("WC_KEY:", wc_key)
# print("WC_SECRET:", wc_secret)
import subprocess

from dotenv import load_dotenv
import os

# Load environment variables from .sh file
load_dotenv("/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh")
subprocess.run(
        'source "/Users/testvagrant/Downloads/Udemy-Python API Testing/api_testing_py_course_material_/env.sh"',
        shell=True)
# Access the environment variables in Python
wc_key = os.environ.get("WC_KEY")
wc_secret = os.environ.get("WC_SECRET")

# Now, you can use wc_key and wc_secret in your test
print("WC_KEY:", wc_key)
print("WC_SECRET:", wc_secret)

