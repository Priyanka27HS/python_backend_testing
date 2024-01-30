#FROM python:latest
#
#MAINTAINER abcd1234@gmail.com
#
#RUN mkdir /automation
#
#COPY ./api_test /automation
#COPY ./setup.py /automation/setup.py
#
#WORKDIR /automation
#
#RUN python3 setup.py install

FROM python:3.11.5

MAINTAINER abcd1234@gmail.com

RUN apt-get update && apt-get -y install vim

# Create a directory for your application
RUN mkdir /automation

# Copy the entire 'api_test' folder into the '/automation' directory
COPY ./api_test /automation/api_test

# Copy 'setup.py' to the '/automation' directory
COPY ./setup.py /automation/setup.py

# Set the working directory to '/automation'
WORKDIR /automation

# Install the 'requests' library
RUN pip install requests
RUN pip install pytest
RUN pip install pytest-html
RUN pip install requests-oauthlib
RUN pip install PyMySQL
RUN pip install WooCommerce
RUN pip install python-dotenv

# Install the dependencies and the application
#RUN python3 setup.py install

# Export the PYTHONPATH environment variable
ENV PYTHONPATH /automation

# Command to run your application (modify as needed)
CMD ["python3", "your_main_script.py"]
