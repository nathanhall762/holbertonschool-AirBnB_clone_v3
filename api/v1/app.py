#!/usr/bin/python3
"""Flask app startup"""
<<<<<<< HEAD
from flask import Flask, jsonify, make_response
=======
from flask import Flask, jsonify
>>>>>>> 14537eac128b3ff756fb6a14e59e1bc46d42d6e1
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """closes app context"""
    storage.close()


@app.errorhandler(404)
<<<<<<< HEAD
def not_found(e):
    return make_response(jsonify({"error": "Not found"}, 404))
=======
def error_404(error):
    """handles 404"""
    return jsonify({
        "error": "Not found"
        })

>>>>>>> 14537eac128b3ff756fb6a14e59e1bc46d42d6e1

if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST', default='0.0.0.0')
    port = environ.get('HBNB_API_PORT', default='5000')
    app.run(host=host, port=port, threaded=True)
