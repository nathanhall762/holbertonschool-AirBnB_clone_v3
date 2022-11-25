#!/usr/bin/python3
"""
view for State objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage, state


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Retrieves all states"""
    state_list = []
    for state in storage.all("State").values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id=None):
    """Retrieves a state"""
    state = storage.get("State", state_id)
    #    return jsonify({})  # return city object of city_id
    if state:
        return jsonify(state.to_dict()), 200
    abort(404)  # a 404 error


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id=None):
    """Deletes a state"""
    state = storage.get("City", state_id)
    #  if:  # id is linked to a city object
    if state:
        state.delete()
        storage.save()
    #    return  # empty dictionary
        return jsonify({}), 200
    #  if:  # id is linked to an empty city object
    abort(404)  # a 404 error


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a state"""
    state = request.get_json(silent=True)
    if state is None:
        abort(400, "Not a JSON")
    elif 'name' not in state.keys():
        abort(400, "Missing name")
    else:
        new_state = state.State(**state)
        storage.new(new_state)
        storage.save()
        return jsonify(state.to_dict()), 201


@app_views.route('/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id=None):
    """Creates a state"""
    abort(404)  # a 404 error
