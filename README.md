vphhf_rest
==========

Implementation of the storage management service for the VPHHF project

# Clone the project
git clone https://github.com/vphhf_rest.git

# Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtualenv
pip install django
pip install djangorestframework

# Let's fire up the server from the command line.
python ./manage.py runserver

# Open the browser
http://localhost:8000/list/


Interact with the APIs using Postman REST client

# GET and POST HTTP methods for the following url
http://localhost:8000/list/

For the POST method use the form-data, select file and write "url" in the key form

# GET and DELETE HTTP methods for the following url
http://localhost:8000/list/#id
