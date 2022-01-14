from flask import Flask

from app.routes.home_route import home_blueprint
from app.routes.salary_route import salary_blueprint
from app.routes.sensor_route import sensor_blueprint
from app.routes.simulation_route import simulation_blueprint

application = Flask(__name__, template_folder='app/views')

application.register_blueprint(home_blueprint)
application.register_blueprint(salary_blueprint)
application.register_blueprint(sensor_blueprint)
application.register_blueprint(simulation_blueprint)

if __name__ == '__main__':
   application.run(debug=True)