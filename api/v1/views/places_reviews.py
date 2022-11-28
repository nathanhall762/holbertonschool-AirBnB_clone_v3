#!/usr/bin/python3
"""
view for review objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review


@app_views.route('/api/v1/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def all_reviews(place_id=None):
    """Retrieves all reviews"""
    s = storage.all(Place)
    review_list = None
    return_list = []
    for p in s.values():
        if p.id == place_id:
            review_list = p.cities
    if review_list is None:
        abort(404)
    for r in review_list:
        return_list.append(r.to_dict())
    return jsonify(return_list)


@app_views.route('/api/v1/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id=None):
    """Retrieves a review"""
    s = storage.get(Review, review_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


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
