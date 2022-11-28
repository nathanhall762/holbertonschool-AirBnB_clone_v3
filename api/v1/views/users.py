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
    #  if:  # id is linked to a user object
    data = storage.get("User", user_id)
    #    return jsonify({})  # return city object of city_id
    if data:
        return jsonify((data.to_dict()))
    abort(404)  # a 404 error


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user():
    """Deletes a user"""
    #  if:  # id is linked to a user object
    #    return jsonify({})  # return all user objects
    #  if:  # id is linked to an empty user object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a user"""
    abort(404)  # a 404 error


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user():
    """Creates a user"""
    abort(404)  # a 404 error
