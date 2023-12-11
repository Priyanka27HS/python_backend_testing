import logging as logger
import random
import string


# this generates some random string
# lets give the user an option to use a domain if they want to and then add a prefix email prefix
# k -> random email links

def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = 'rpxyz.com'
    if not email_prefix:
        email_prefix = 'testapiuser17'

    random_email_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password : {random_info}")

    return random_info


# function that will generate a random string
def generate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string
