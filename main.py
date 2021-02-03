from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import pymysql.cursors  
import time
import json
import re
from datetime import datetime
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
logging.basicConfig(filename='request.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.route('/sendmessage/api/v1.0/', methods=['GET'])
def sendmessage_v1_0():
    connection = pymysql.connect(
    host =  "127.0.0.1",
    port =  3306,
    user = "socialuser",
    passwd = "socialpass",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor,
    database = "social")

    message_from = request.args.get('message_from') 
    message_to = request.args.get('message_to')
    message_text = request.args.get('message_text')
    message_date = request.args.get('message_date')
    requestid = request.args.get('requestid')
    logging.warning("message date: "+ message_date + " | message_from: " + message_from + " | message_to: " + message_to + " | message_text: " +  message_text + " | requestid: " + requestid )
    try:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO dialogs (  message_from, message_to ,message_text ,message_date )   VALUES(%s, %s, %s, %s) ', ( message_from, message_to, message_text, message_date),)
        connection.commit()
    finally:
        connection.close()
    return  "message recieved"
    
@app.route('/sendmessage/api/v0.0/', methods=['GET'])
def sendmessage_v0_0():
    connection = pymysql.connect(
    host =  "127.0.0.1",
    port =  3306,
    user = "socialuser",
    passwd = "socialpass",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor,
    database = "social")

    message_from = request.args.get('message_from') 
    message_to = request.args.get('message_to')
    message_text = request.args.get('message_text')
    message_date = request.args.get('message_date')
    requestid = request.args.get('requestid')
    logging.warning("message date: "+ message_date + " | message_from: " + message_from + " | message_to: " + message_to + " | message_text: " +  message_text + " | requestid: " + requestid )
    try:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO dialogs (  message_from, message_to ,message_text ,message_date )   VALUES(%s, %s, %s, %s) ', ( message_from, message_to, message_text, message_date),)
        connection.commit()
    finally:
        connection.close()
    return  "message recieved"



    


if __name__ == "__main__":
    application.run(debug=True,host='0.0.0.0')
