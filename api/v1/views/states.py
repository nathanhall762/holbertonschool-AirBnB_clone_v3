#!/usr/bin/python3
"""
view for State objects that handles all default RESTful API actions
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Retrieves all states"""
    if:  # exists
        return jsonify({})  # return all state objects
    return  # a 404 error


@app_views.route('/api/v1/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state():
    """Retrieves a state"""
    if:  # id is linked to a State object
        return jsonify({})  # return State object of state_id
    return  # a 404 error


@app_views.route('/api/v1/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state():
    """Deletes a state"""
    if:  # id is linked to a State object
        return jsonify({})  # return all state objects
    if:  # id is linked to an empty state object
        return  # empty dictionary
    return  # a 404 error


@app_views.route('/api/v1/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a state"""
    return  # a 404 error


@app_views.route('/api/v1/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """Creates a state"""
    return  # a 404 error
