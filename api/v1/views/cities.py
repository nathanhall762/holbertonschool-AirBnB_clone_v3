#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities(state_id):
    """Retrieves all cities"""
    s = storage.all(State)
    cities_list = None
    return_list = []
    for state in s.values():
        if state.id == state_id:
            cities_list = state.cities
    if cities_list is None:
        abort(404)
    for city in cities_list:
        return_list.append(city.to_dict())
    return jsonify(return_list)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Retrieves a city"""
    s = storage.get(City, city_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id=None):
    """Deletes a city"""
    s = storage.get(City, city_id)
    if s is None:
        abort(404)  # a 404 error
    storage.delete(s)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Creates a city"""
    state = storage.get(State, state_id)
    update = request.get_json(silent=True)
    if not update:
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in update:
        return jsonify({'error': 'Missing Name'}), 400
    if state:
        update['state_id'] = state_id
        city = City(**update)
        city.save()
        return jsonify(city.to_dict()), 201
    abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a city"""
    city_dict = request.get_json()
    if not city_dict:
        return (jsonify({"error": "Not a JSON"}), 400)
    city = storage.get("City", city_id)
    if city:
        city.name = city_dict['name']
        city.save()
        return (jsonify(city.to_dict()), 200)
    abort(404)  # a 404 error
