from flask import Blueprint, request

home_blueprint = Blueprint('home_route', __name__)

@home_blueprint.route('/', methods=['GET'])
def create_home():
    return "Home Page"