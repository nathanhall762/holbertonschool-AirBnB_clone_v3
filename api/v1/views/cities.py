#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities():
    """Retrieves all cities"""
    #  if:  # exists
    #    return jsonify({})  # return all city objects
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Retrieves a city"""
    # if:  # id is linked to a city object
    cities = storage.get("City", city_id)
    #    return jsonify({})  # return city object of city_id
    if cities:
        return jsonify((cities.to_dict(), 200))
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a city"""
    city = storage.get("City", city_id)
    #  if:  # id is linked to a city object
    if city:
        city.delete()
        storage.save()
    #    return  # empty dictionary
        return (jsonify({}), 200)
    #  if:  # id is linked to an empty city object
    abort(404)  # a 404 error


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city():
    """Creates a city"""
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city():
    """Creates a city"""
    abort(404)  # a 404 error
