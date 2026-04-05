import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Nate Bliton in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab_10_db_dvqw_user:J931DPwmHL8EHhkXL810pNeiLDZcgQfC@dpg-d79e5s6a2pns73e3fjn0-a/lab_10_db_dvqw")

    conn.close()
    return "Databse Connection Successful"