Flask app that redirects to the most relevant YouTube video based on a given
query.

Getting started
===============

Requirements:

* flask

This requirement is expressed in the `requirements.txt` file and may be
installed by running the following command (preferably from a virtual
environment)::

    pip install -r requirements.txt

Usage
=====

Execute the script to start werkzeug on `localhost:5000`, or serve through
WSGI.

The query should be URL encoded, for example:
http://localhost:5000/goats+yelling+like+humans

