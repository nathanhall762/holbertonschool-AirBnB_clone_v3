#!/usr/bin/python3
"""
view for review objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from sqlalchemy.exc import IntegrityError


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def all_reviews(place_id):
    """Retrieves all reviews"""
    s = storage.all(Place)
    review_list = None
    return_list = []
    for p in s.values():
        if p.id == place_id:
            review_list = p.reviews
    if review_list is None:
        abort(404)
    for r in review_list:
        return_list.append(r.to_dict())
    return jsonify(return_list)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """Retrieves a review"""
    s = storage.get(Review, review_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id=None):
    """Deletes a review"""
    s = storage.get(Review, review_id)
    if s is None:
        abort(404)  # a 404 error
    storage.delete(s)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """Creates a review"""
    try:
        p = storage.get(Place, place_id)
        update = request.get_json(silent=True)
        if not update:
            return jsonify({'error': 'Not a JSON'}), 400
        elif 'text' not in update:
            return jsonify({'error': 'Missing text'}), 400
        elif 'user_id' not in update:
            return jsonify({'error': 'Missing user_id'}), 400
        if p:
            update['place_id'] = place_id
            city = Review(**update)
            city.save()
            return jsonify(city.to_dict()), 201
        abort(404)
    except IntegrityError:
        abort(404)


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Creates a review"""
    review_dict = request.get_json(silent=True)
    if not review_dict:
        return (jsonify({"error": "Not a JSON"}), 400)
    r = storage.get(Review, review_id)
    if r:
        for key, value in r.items():
            if key not in ['id', 'user_id', 'place_id',
                           'created_at', 'updated_at']:
                setattr(review_dict, key, value)
        storage.save()
        try:
            return make_response(jsonify(r.to_dict()), 200)
        except:
            return ''
    abort(404)  # a 404 error
