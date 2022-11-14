import json
from flask_jwt_extended import create_access_token
import requests
from flask import jsonify
from datetime import  timedelta


class ControladorSeguridad():
    """Clase que implementa el controlador para los endpoints relacionado con los estudiante"""
    def __init__(self):
        print("\t>>Creando controlador de seguridad")
        self.dataConfig = self.__loadFileConfig()
       

    def login(self,data): #los lista todos los estudiantes 
        print("\t>>Login" + str(data))
        # logica de verificación de usuario
        #1. Consumir el servicio de validación de usuario del microservicio de seguridad
        headers = {"Content-Type":"application/json; charset=utf-8"}
        url= self.dataConfig=["url-backend-security"]+'/usuarios/validar'
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            user = response.json()
            expires = timedelta(seconds=60 * 60*24)
            access_token = create_access_token(identity=user, expires_delta = expires)
            return jsonify ({"token": access_token, "user_id": user["_id"]})
        else:
            return jsonify ({"msg": "Bad username or password"}), 401


    def __loadFileConfig(self):
        with open ('config.json') as f:
            data = json.load(f)
        return data

    