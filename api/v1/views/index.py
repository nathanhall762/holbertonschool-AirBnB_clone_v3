#!/usr/bin/python3
"""documentation"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('views/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Retrieves OK message"""
    return jsonify({
        'status': 'OK'
    })


@app_views.route('views/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of objects by type"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
