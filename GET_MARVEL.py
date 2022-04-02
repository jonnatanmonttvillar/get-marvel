from flask import request, jsonify, Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine 
from json import dumps
import hashlib
import requests

db_connect = create_engine('sqlite:///C:/Users/vina/Documents/Api-Marvel')
app = Flask(__name__)
API = Api(app)

def main_api():
    public = 'dd3fc84ce882e4261cac1773aa763ec4'
    private = '418ca09585d90348bb7bba6753c202ded59b382e'
    ts = "1"
    hash = hashlib.md5((ts + private + public).encode()).hexdigest()
    base  = 'http://gateway.marvel.com/v1/public/'
    caracter = requests.get(base + 'characters',
                           params = {'apikey' : public, 'ts' : ts, 'hash' : hash,
                                     'name' : 'wolverine'}).json()
    print(caracter)

if __name__ == '__main__':
    main_api()