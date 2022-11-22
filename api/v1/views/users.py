#!/usr/bin/python3
"""
view for user objects that handles all default RESTful API actions
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Retrieves all users"""
    if:  # exists
        return jsonify({})  # return all user objects
    return  # a 404 error


@app_views.route('/api/v1/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user():
    """Retrieves a user"""
    if:  # id is linked to a user object
        return jsonify({})  # return user object of user_id
    return  # a 404 error


@app_views.route('/api/v1/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user():
    """Deletes a user"""
    if:  # id is linked to a user object
        return jsonify({})  # return all user objects
    if:  # id is linked to an empty user object
        return  # empty dictionary
    return  # a 404 error


@app_views.route('/api/v1/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a user"""
    return  # a 404 error


@app_views.route('/api/v1/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user():
    """Creates a user"""
    return  # a 404 error
