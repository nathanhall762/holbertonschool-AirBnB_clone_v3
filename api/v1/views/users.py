#!/usr/bin/python3
"""
view for user objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route('/api/v1/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Retrieves all users"""
    #  if:  # exists
    #    return jsonify({})  # return all user objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """Retrieves a user"""
    #  if:  # id is linked to a user object
    data = storage.get("User", user_id)
    #    return jsonify({})  # return city object of city_id
    if data:
        return jsonify((data.to_dict()))
    abort(404)  # a 404 error


@app_views.route('/api/v1/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user():
    """Deletes a user"""
    #  if:  # id is linked to a user object
    #    return jsonify({})  # return all user objects
    #  if:  # id is linked to an empty user object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/api/v1/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a user"""
    abort(404)  # a 404 error


@app_views.route('/api/v1/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user():
    """Creates a user"""
    abort(404)  # a 404 error
