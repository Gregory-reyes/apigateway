from datetime import datetime, timedelta, timezone
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import json
from waitress import serve

import Endpoints

app=Flask(__name__)
cors = CORS(app)

app.config["JWT_SECRET_KEY"]="super-secret" #cambiar por el que sea conveniente
jwt = JWTManager(app)

#Registro de Endpoints
app.register_blueprint(Endpoints.endpointSeguridad)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    __uptime = datetime.now(timezone(-timedelta(hours=5)))- __init_time
    json["message"]="Server running ..."
    json["uptime"]= f'{__uptime}'
    return jsonify(json)

__init_time = None
if __name__=='__main__':
    dataConfig = loadFileConfig()
print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
__init_time = datetime.now(timezone(-timedelta(hours=5)))
print(f'Init time:{__init_time}')
serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])