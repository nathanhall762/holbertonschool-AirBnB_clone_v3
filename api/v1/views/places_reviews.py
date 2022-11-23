#!/usr/bin/python3
"""
view for review objects that handles all default RESTful API actions
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/api/v1/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def all_reviews():
    """Retrieves all reviews"""
    #  if:  # exists
    #    return jsonify({})  # return all review objects
    abort(404)  # a 404 error


@app_views.route('/api/v1/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review():
    """Retrieves a review"""
    #  if:  # id is linked to a review object
    #    return jsonify({})  # return review object of review_id
    abort(404)  # a 404 error


@app_views.route('/api/v1/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review():
    """Deletes a review"""
    #  if:  # id is linked to a review object
    #    return jsonify({})  # return all review objects
    #  if:  # id is linked to an empty review object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/api/v1/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_review():
    """Creates a review"""
    abort(404)  # a 404 error


@app_views.route('/api/v1/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def update_review():
    """Creates a review"""
    abort(404)  # a 404 error
