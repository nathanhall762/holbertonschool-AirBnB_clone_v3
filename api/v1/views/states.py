#!/usr/bin/python3
"""
view for State objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route('/api/v1/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Retrieves all states"""
    #  if:  # exists
    #     return jsonify({})  # return all state objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Retrieves a state"""
    state = storage.get("City", state_id)
    #    return jsonify({})  # return city object of city_id
    if state:
        return (jsonify(state.to_dict()), 200)
    abort(404)  # a 404 error


@app_views.route('/api/v1/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state():
    """Deletes a state"""
    # if:  # id is linked to a State object
    #    # return jsonify({})  # return all state objects
    # if:  # id is linked to an empty state object
    #    # return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/api/v1/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a state"""
    abort(404)  # a 404 error


@app_views.route('/api/v1/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """Creates a state"""
    abort(404)  # a 404 error
