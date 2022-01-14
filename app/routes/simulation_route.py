from flask import Blueprint, request

simulation_blueprint = Blueprint('simulation_route', __name__)

@simulation_blueprint.route('/simulation', methods=['GET'])
def create_home():
    return "Simulation Page"