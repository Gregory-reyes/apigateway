import json
import requests
from flask import jsonify



class ControladorInscripciones():
    """Clase que implementa el controlador para los endpoints relacionado con los estudiante"""
    def __init__(self):
        print("\t>>Creando controlador de inscripciones")
        self.dataConfig = self.__loadFileConfig()
       

    def idex(self): #los lista todos los estudiantes 
        print("\t>>Inscripciones-Index" )
        # logica de verificación de usuario
        #1. Consumir el servicio de validación de usuario del microservicio de seguridad
        _headers = {"Content-Type":"application/json; charset=utf-8"}
        url= self.dataConfig=["url-backend-security"]+'/usuarios/inscripciones'
        response = requests.get(url, headers=_headers)
        if response.status_code == 200:
            json = response.json()            
            return json
        else:
            return ({"msg": "Bad username or password"}), 401


    def __loadFileConfig(self):
        with open ('config.json') as f:
            data = json.load(f)
        return data
