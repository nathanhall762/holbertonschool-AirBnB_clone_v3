#!/usr/bin/python3
"""
view for Amenity objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/api/v1/amenities', methods=['GET'], strict_slashes=False)
def all_amenities():
    """Retrieves all amenities"""
    #  if:  # exists
    #    return jsonify({})  # return all amenity objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a amenity"""
    #  if:  # id is linked to a amenity object
    data = storage.get("Amenity", amenity_id)
    #    return jsonify({})  # return city object of city_id
    if data:
        return jsonify((data.to_dict(), 200))
    abort(404)  # a 404 error


@app_views.route('/api/v1/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity():
    """Deletes a amenity"""
    #  if:  # id is linked to a amenity object
    #    return jsonify({})  # return all amenity objects
    #  if:  # id is linked to an empty amenity object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/api/v1/amenities', methods=['POST'], strict_slashes=False)
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


@app_views.route('/api/v1/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
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
