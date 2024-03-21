from flask import Flask, request
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')