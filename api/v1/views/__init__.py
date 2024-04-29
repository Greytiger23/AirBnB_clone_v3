#!/usr/bin/python3
""" int it file"""


from flask import Blueprint
from flask_cors import CORS
from .index import *
from .states import *
# import app_views after defining it
import api.v1.views.index
import api.v1.views.states

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
CORS(app_views)
