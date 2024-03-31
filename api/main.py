from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import datetime

app = Flask(__name__)

db_cred = { 
    'user': '<DATABASE USER>',         # DATABASE USER 
    'pass': '<DATABASE PASSWORD>',     # DATABASE PASSWORD 
    'host': '<DATABASE HOSTNAME>',    # DATABASE HOSTNAME 
    'name': '<DATABASE_NAME>'   # DATABASE NAME 
} 

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_cred['user']}:{db_cred['pass']}@{db_cred['host']}:5432/{db_cred['name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db  = SQLAlchemy(app) 

winter_months = [1,2,3,11,12]
autumn_months = [9,10]
spring_months = [4,5]
summer_months = [6,7,8]

@app.route("/")
def index():
    return "<h1 style='color:blue'>Hello There-DEV</h1>"

@app.route("/dht11")
def foo():
    temperature = request.args.get("t")
    humidity = request.args.get("h")

    with db.engine.connect() as con:
        con.execute(text(f'''INSERT INTO dht11(humidity, temperature, date) VALUES ({int(humidity)}, {int(temperature)}, '{datetime.datetime.now()}')'''))
        con.commit()
    

    return f"<h1 style='color:blue'>{temperature} - {humidity}</h1>"

@app.route("/last")
def last():
    temp = 23
    hum = 10
    light = 10

    data = {
        "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "temperature":{
            "value": temp,
            "category": GetWarningLevel(temp)
        },
        "humidity":{
            "value": hum,
            "category": GetWarningLevel(hum)
        },
        "light":{
            "value": light,
            "category": GetWarningLevel(light)
        },
    }
    return jsonify(data)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

def GetWarningLevel(temperature):
    
    month = datetime.datetime.now().month

    if month in winter_months:
        if temperature < 20:
            return "danger"
        elif temperature >= 20 and temperature <= 22:
            return "warning"
        else:
            return "normal"
        
    if month in summer_months:
        if temperature > 28:
            return "danger"
        elif temperature >=26 and temperature <=28:
            return "warning"
        else:
            return "normal"
        
    if temperature < 15 or temperature > 28:
        return "danger"
    else: 
        return "normal"

if __name__ == "__main__":
    app.run(host='0.0.0.0')