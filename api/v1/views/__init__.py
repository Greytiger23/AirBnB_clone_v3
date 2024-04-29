#!/usr/bin/python3
""" int it file"""


from flask import Blueprint
from flask_cors import CORS

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
CORS(app_views)

from .index import *
from .states import *

# import app_views
from api.v1.views import app_views
