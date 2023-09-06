from flask import*
import os
import mysql.connector 
import pymysql
import random
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
db_user = 'ingmen-central-db'
db_password= 'astartup@2023'
db_name = 'ingman-primary'
db_connection_name = 'fresh-sanctuary-397904:us-west1:ingmen-central-db'

def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        # if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(
                user = db_user,
                password = db_password,
                unix_socket = unix_socket,
                cursorclass = pymysql.cursors.DictCursor
            )
    except pymysql.MySQLError as e:
            return e
    return conn

connection = open_connection()
d = connection.execute("select * from ingman-primary")
data = cursor.fetchall()