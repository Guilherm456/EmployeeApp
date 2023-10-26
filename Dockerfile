FROM python:3.10

# Create app directory
RUN mkdir /employee_service

WORKDIR /employee_service

ADD . /employee_service/

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000