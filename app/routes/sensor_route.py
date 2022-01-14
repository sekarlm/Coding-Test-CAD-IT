from flask import Blueprint, request

sensor_blueprint = Blueprint('sensor_route', __name__)

@sensor_blueprint.route('/sensor', methods=['GET'])
def create_home():
    return "Sensor Page"