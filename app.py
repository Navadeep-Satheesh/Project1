from flask import*
import mysql.connector 
import random
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
db = "project2"
password = "ashvin2004"
connection = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password =   password ,
    db = db
)
cursor = connection.cursor( buffered=True)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/')
def index():
    return render_template('home.html')

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

            cursor.execute(f"INSERT INTO users (PersonID , user_name , Ph, email) VALUES ('{user_id}','{name}' , '{mobile_number}','{email}');")
            connection.commit()
            return ('' , 204)

    
        else:
            message = "Error,user already exist"
            return jsonify(message)
        
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

        


if __name__ == "__main__":
    app.run(debug = True)
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