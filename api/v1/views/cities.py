#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities():
    """Retrieves all cities"""
    c = storage.get("State", state_id)
    cities_list = []
    for city in c.cities.values():
        cities_list.append(city.to_dict())
    return jsonify(cities_list)

    # # s = storage.all(City)
    # # cities_list = []
    # # for city in s.cities.values():
    # #     cities_list.append(city.to_dict())
    # # return jsonify(cities_list)
    # abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Retrieves a city"""
    # s = storage.get(City, city_id)
    # if s is None:
    #     abort(404)  # a 404 error
    # return jsonify(s.to_dict()), 200


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id=None):
    """Deletes a city"""
    # s = storage.get(City, city_id)
    # if s is None:
    #     abort(404)  # a 404 error
    # storage.delete(s)
    # storage.save()
    # return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id=None):
    """Creates a city"""
    # city = storage.get(City, state_id)
    # if city is None:
    #     abort(404)
    # update = request.get_json(silent=True)
    # if update is None:
    #     abort(400, "Not a JSON")
    # else:
    #     for key, value in update.items():
    #         if key in ['id', 'created_at', 'updated_at']:
    #             pass
    #         else:
    #             setattr(city, key, value)
    #     storage.save()
    #     response = city.to_dict()
    #     return make_response(jsonify(response), 200)


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
