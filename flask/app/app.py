from flask import Flask, request, redirect, url_for, flash, jsonify, abort, Response
#from flask_cors import CORS
import warnings
import os
import time
import datetime

warnings.filterwarnings("ignore")

app = Flask(__name__)

#CORS(app) #Prevents CORS errors

url_prefix = os.getenv('baseUrl','blabla')

@app.route('/', methods=['POST','GET'])
def default_route():
	time.sleep(10)
	return 'works!' + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

@app.route('/'+url_prefix+'/', methods=['POST','GET'])
def default_baseURL():
	time.sleep(10)
	return 'works!' + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

if __name__ == '__main__':
    app.run(host='0.0.0.0')