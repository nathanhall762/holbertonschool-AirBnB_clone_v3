#!/usr/bin/python3
"""
view for place objects that handles all default RESTful API actions
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def all_places():
    """Retrieves all places"""
    if:  # exists
        return jsonify({})  # return all place objects
    return  # a 404 error


@app_views.route('/api/v1/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place():
    """Retrieves a place"""
    if:  # id is linked to a place object
        return jsonify({})  # return place object of place_id
    return  # a 404 error


@app_views.route('/api/v1/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place():
    """Deletes a place"""
    if:  # id is linked to a place object
        return jsonify({})  # return all place objects
    if:  # id is linked to an empty place object
        return  # empty dictionary
    return  # a 404 error


@app_views.route('/api/v1/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place():
    """Creates a place"""
    return  # a 404 error


@app_views.route('/api/v1/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place():
    """Creates a place"""
    return  # a 404 error
