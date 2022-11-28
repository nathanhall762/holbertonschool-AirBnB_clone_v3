#!/usr/bin/python3
"""
view for Amenity objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def all_amenities():
    """Retrieves all amenities"""
    s = storage.all(Amenity)
    state_list = []
    for state in s.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id=None):
    """Retrieves a amenity"""
    state = storage.get(Amenity, amenity_id)
    if state is None:
        abort(404)  # a 404 error
    return jsonify(state.to_dict()), 200


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id=None):
    """Deletes a state"""
    state = storage.get(Amenity, state_id)
    if state is None:
        abort(404)  # a 404 error
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a amenity"""
    req = request.get_json(silent=True)
    if req is None:
        abort(400, "Not a JSON")
    if 'name' not in req.keys():
        abort(400, "Missing name")
    new_state = Amenity(**req)
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id=None):
    """Creates a amenity"""
    state = storage.get(Amenity, amenity_id)
    if state is None:
        abort(404)
    update = request.get_json(silent=True)
    if update is None:
        abort(400, "Not a JSON")
    else:
        for key, value in update.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(state, key, value)
        storage.save()
        response = state.to_dict()
        return make_response(jsonify(response), 200)
