from flask import render_template

import os
import json
import requests

BASE_DIR = os.getcwd()
DATA_PATH = BASE_DIR + '/app/data/'

class SalaryController:
    def create_salary(self):
        with open(DATA_PATH+'salary_data.json') as json_file:
            data = json.load(json_file)
        
        salaries = data["array"]
        req = 
        return render_template('/layouts/salary.html')