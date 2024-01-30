from setuptools import setup, find_packages

setup(name='api_test',
      version='1.0',
      description="Practice API Testing",
      author='Priyanka',
      author_email='abcd1234@gmail.com',
      url='https://www.w3schools.com/python/',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest",
          "pytest-html",
          "requests",
          "requests-oauthlib",
          "PyMySQL",
          "WooCommerce",
      ]
)
