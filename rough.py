# from flask import*
# import os
# import mysql.connector 
# import pymysql
# import random
# from flask import Flask, render_template, redirect, request, session
# from flask_session import Session
# import os
# import google
# from google.cloud.sql.connector import Connector, IPTypes
# import pg8000

# import sqlalchemy

# db_user = 'ingmen-central-db'
# db_password= 'astartup@2023'
# db_name = 'ingman-primary'
# db_connection_name = 'fresh-sanctuary-397904:us-west1:ingmen-central-db'

# # def open_connection():
# #     unix_socket = '/cloudsql/{}'.format(db_connection_name)
# #     try:
# #         # if os.environ.get('GAE_ENV') == 'standard':
# #             conn = pymysql.connect(
# #                 user = db_user,
# #                 password = db_password,
# #                 unix_socket = unix_socket,
# #                 cursorclass = pymysql.cursors.DictCursor
# #             )
# #     except pymysql.MySQLError as e:
# #             return e
# #     return conn




# def connect_with_connector() -> sqlalchemy.engine.base.Engine:
#     """
#     Initializes a connection pool for a Cloud SQL instance of Postgres.

#     Uses the Cloud SQL Python Connector package.
#     """
#     # Note: Saving credentials in environment variables is convenient, but not
#     # secure - consider a more secure solution such as
#     # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
#     # keep secrets safe.

#     instance_connection_name = os.environ[
#         "INGMEN PROJECT:fresh-sanctuary-397904:us-west1:ingmen-central-db"
#     ]  # e.g. 'project:region:instance'
#     db_user = os.environ["db_user"]  # e.g. 'my-db-user'
#     db_pass = os.environ["db_password"]  # e.g. 'my-db-password'
#     db_name = os.environ["ingman-primary"]  # e.g. 'my-database'

#     ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

#     # initialize Cloud SQL Python Connector object
#     connector = Connector()

#     def getconn() -> pg8000.dbapi.Connection:
#         conn: pg8000.dbapi.Connection = connector.connect(
#             instance_connection_name,
#             "pg8000",
#             user=db_user,
#             password=db_pass,
#             db=db_name,
#             ip_type=ip_type,
#         )
#         return conn

# connection = Connector
# cursor = connection.cursor( buffered=True)
# d = connection.execute("select * from ingman-primary")
# data = cursor.fetchall()


# from flask import*
# import mysql.connector 
# import random
# from flask import Flask, render_template, redirect, request, session
# from flask_session import Session

# from google.cloud.sql.connector import Connector, IPTypes
# import sqlalchemy
# import pymysql

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


# data = cursor.execute("SELECT * FROM users").fetchall()
# print(data)


#############\


import sqlite3
# from google.cloud import storage
import mysql.connector
import sys

connection = mysql.connector.connect(user = 'ingmen-central-db' , password = 'astartup@2023' , host = '34.168.106.137' , database = 'ingman-primary')
# connection = mysql.connector.connect(user = 'test' , password = 'test1234' , host = '34.168.106.137' , database = 'testdb')
cursor = connection.cursor()
cursor.execute('select * from users')
data = cursor.fetchall()
print(data)