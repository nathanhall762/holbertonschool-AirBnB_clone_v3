#!/usr/bin/python3
"""Flask app startup"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST', default='0.0.0.0')
    port = environ.get('HBNB_API_PORT', default='5000')
    app.run(host=host, port=port, threaded=True)
