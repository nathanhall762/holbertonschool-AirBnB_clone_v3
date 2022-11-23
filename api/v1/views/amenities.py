#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/api/v1/amenities', methods=['GET'], strict_slashes=False)
def all_amenities():
    """Retrieves all amenities"""
    #  if:  # exists
    #    return jsonify({})  # return all amenity objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity():
    """Retrieves a amenity"""
    #  if:  # id is linked to a amenity object
    #    return jsonify({})  # return amenity object of amenity_id
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
    abort(404)  # a 404 error


@app_views.route('/api/v1/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity():
    """Creates a amenity"""
    abort(404)  # a 404 error
