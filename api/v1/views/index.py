#!/usr/bin/python3
"""documentation"""
from api.v1.views import app_views


@app_views.route('views/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of objects by type"""
    objects_count_dict = {
        "amenities": 47,
        "cities": 36,
        "places": 154,
        "reviews": 718,
        "states": 27,
        "users": 31
    }
    return objects_count_dict
