#!/usr/bin/python3
"""
view for user objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Retrieves all users"""
    s = storage.all(User)
    state_list = []
    for state in s.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """Retrieves a user"""
    s = storage.get(User, user_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id=None):
    """Deletes a user"""
    s = storage.get(User, user_id)
    if s is None:
        abort(404)  # a 404 error
    storage.delete(s)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a user"""
    req = request.get_json(silent=True)
    if req is None:
        abort(400, "Not a JSON")
    if 'email' not in req.keys():
        abort(400, "Missing email")
    if 'password' not in req.keys():
        abort(400, "Missing password")
    new_state = User(**req)
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user():
    """Creates a user"""
    abort(404)  # a 404 error
