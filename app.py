from flask import*
import mysql.connector 
import random
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import os
import requests
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import pymysql

# connector = Connector()

# def getconn():
#     conn = connector.connect(
#         "fresh-sanctuary-397904:us-west1:ingmen-central-db",
#         "pymysql",
#         user="test",
#         password="test1234",
#         db="testdb",
#         ip_type=IPTypes.PUBLIC
#     )
    
#     return conn


# cursor = sqlalchemy.create_engine(
#     "mysql+pymysql://",
#     creator=getconn,
# )
# with cursor.connect() as cursor:


# #result = pool.execute("show tables").fetchall()
#     result = cursor.execute("show tables").fetchall()

import sqlite3
# from google.cloud import storage
import mysql.connector
import sys

connection = mysql.connector.connect(user = 'ingmen-central-db' , password = 'astartup@2023' , host = '34.168.106.137' , database = 'ingman-primary')
# connection = mysql.connector.connect(user = 'test' , password = 'test1234' , host = '34.168.106.137' , database = 'testdb')
cursor = connection.cursor()


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/')
def index():
    return jsonify("hiiii get lost")



@app.route('/entry', methods =['POST'])
def entry():
    if request.method == 'POST':
        d = request.json
        print(d)
        cursor.execute(f"SELECT * FROM users ")
        data = cursor.fetchall()
        print(data)
        try:

            u = data[-1]
            print(u)
            user_id = u[0]+1
        except:
            user_id = 1
        
        
        print (f"user id is {user_id}")
        print(user_id)
        
        
        
        name,mobile_number,email =  d["user_name"], d["mobile_number"],d["email"]
        cursor.execute(f"SELECT * FROM users WHERE ph = '{mobile_number}'")
        data = cursor.fetchall()
        print(d)
        
        
        
        
        print(user_id)
        
        if len(data) == 0 :

            cursor.execute(f"INSERT INTO users (PersonID , user_name ,ph, email) VALUES ('{user_id}','{name}' , '{mobile_number}','{email}');")
            connection.commit()
            return ('' , 204)

    
        else:
            cursor.execute(f"UPDATE users SET  user_name = '{name}', email= '{email}' WHERE ph = '{mobile_number}';")
            connection.commit()
            return ('' , 204)
        
@app.route('/send_otp', methods =['POST'])     
def otp():
    otp = ""
    d = request.json
    
    ph = d["1"]
    for no in range(6):  
        otp += str(random.randint(1,9))
     # send sms(otp)
    # print(otp)
    session[ph] = otp
    
    return ('' , 204)

@app.route('/check_otp', methods =['POST'])
def checker():
    otp = ""
    d = request.json
    ph = list(d.keys())[0] 
    entered_otp = d[ph]
    print(entered_otp)

    if entered_otp == session.get(ph):
        print("true")
        return ('' , 204)
    
    else:
        message = "OTP missmatch"
        return jsonify(message)



        

@app.route('/address', methods =['POST'])
def address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip = response.text
    return ip

if __name__ == "__main__":
    app.run(debug = True,  host = "0.0.0.0" , port = 8080)
#git init
# git commit -m "first commit"
# git branch -M main
# git push -u origin main


#####
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/ashvxn/Project1.git
# git push -u origin main
