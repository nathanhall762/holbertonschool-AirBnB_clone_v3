#!/usr/bin/python3
"""init file for views directory"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(url_prefix="/api/v1")
