from flask import Blueprint

bp = Blueprint('entries', __name__)

from blueprints.entries import forms