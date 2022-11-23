#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route('/api/v1/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities():
    """Retrieves all cities"""
    #  if:  # exists
    #    return jsonify({})  # return all city objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Retrieves a city"""
    # if:  # id is linked to a city object
    data = storage.get("City", city_id)
    #    return jsonify({})  # return city object of city_id
    if data:
        return jsonify((data.to_dict(), 200))
    abort(404)  # a 404 error


@app_views.route('/api/v1/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city():
    """Deletes a city"""
    #  if:  # id is linked to a city object
    #    return jsonify({})  # return all city objects
    #  if:  # id is linked to an empty city object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/api/v1/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city():
    """Creates a city"""
    abort(404)  # a 404 error


@app_views.route('/api/v1/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city():
    """Creates a city"""
    abort(404)  # a 404 error
