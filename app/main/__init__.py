from app.auth import forms
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views