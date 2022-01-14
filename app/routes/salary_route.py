from flask import Blueprint, request
from app.controllers.salary_controller import SalaryController
salary_blueprint = Blueprint('salary_route', __name__)

@salary_blueprint.route('/salary', methods=['GET'])
def create_home():
    return SalaryController().create_salary()