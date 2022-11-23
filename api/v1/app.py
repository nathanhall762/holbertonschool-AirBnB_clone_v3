#!/usr/bin/python3
"""Flask app startup"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import environ
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='0.0.0.0')
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes app context"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """adding handler for error"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST', default='0.0.0.0')
    port = environ.get('HBNB_API_PORT', default='5000')
    app.run(host=host, port=port, threaded=True)
