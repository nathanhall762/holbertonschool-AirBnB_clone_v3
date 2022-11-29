#!/usr/bin/python3
"""
view for place objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def all_places(city_id):
    """Retrieves all places"""
    s = storage.all(City)
    place_list = None
    return_list = []
    for city in s.values():
        if city.id == city_id:
            place_list = city.places
    if place_list is None:
        abort(404)
    for place in place_list:
        return_list.append(place.to_dict())
    return jsonify(return_list)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id=None):
    """Retrieves a place"""
    s = storage.get(Place, place_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id=None):
    """Deletes a place"""
    s = storage.get(Place, place_id)
    if s is not None:
        storage.delete(s)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Creates a place"""
    city_dict = storage.get(City, city_id)
    update = request.get_json(silent=True)
    if not update:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in update.keys:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    if 'user_id' not in update:
        return jsonify({'error': 'Missing user_id'}), 400
    if city_dict:
        update['city_id'] = city_id
        place = Place(**update)
        place.save()
        return make_response(jsonify(place.to_dict()), 201)
    abort(404)


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Creates a place"""
    state = storage.get(Place, place_id)
    if state is None:
        abort(404)
    update = request.get_json(silent=True)
    if update is None:
        abort(400, "Not a JSON")
    else:
        for key, value in update.items():
            if key in ['id', 'user_id', 'place_id',
                       'created_at', 'updated_at']:
                pass
            else:
                setattr(state, key, value)
        storage.save()
        response = state.to_dict()
        return make_response(jsonify(response), 200)
