import json
import re
from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity
import requests
from flask import jsonify, request



class ControladorMiddleware():
    """Clase que implementa el controlador para los endpoints relacionado con los estudiante"""
    def __init__(self):
        print("\t>>Creando controlador de Middleware")
        self.dataConfig = self.__loadFileConfig()       

    def before_request_func(self): #los lista todos los estudiantes 
        print("\t\t>>BEFORE")
        endPoint = self.__limpiarURL(request.path)
        excludeRoutes = ["/","/login"]
        if excludeRoutes.__contains__(request.path):
            print("ruta exluida", request.path)
            pass
        elif verify_jwt_in_request():
            usuario = get_jwt_identity()
            if usuario["rol"]is not None:
                tienePermiso = self.__validarPermiso(endPoint,request.method,usuario["rol"]["tipo"])
                if not tienePermiso:
                    return jsonify({"message":"Permiso denied"}),401
            else:
                return jsonify ({"message": "Permiso denied el usario no tiene un rol asociado"}), 403

    
    def alfer_request_func(self,response): #los lista todos los estudiantes 
        print("\t\t>>AFTER")
        return response

    def __limpiarURL(self,url):
        partes= request.path.split("/")
        for laParte in partes:
            if re.search('\\d',laParte):
                url = url.replace(laParte, "?")
        return url
    def __validarPermiso(self,endPoint,metodo,rol):
        url = self.dataConfig["url-backend-security"+"/permisosrol/validar/"+str(rol)]
        tienePermiso= False
        headers = {"Content-Type": "application/json; charset=utf-8"}
        body = {"url":endPoint, "metodo":metodo}
        response = request.get(url,json=body, headers=headers)
        try:
            data = response.json()
            if("id" in data):
                tienePermiso = True
        except:
            pass
        return  tienePermiso

    def __loadFileConfig(self):
        with open ('config.json') as f:
            data = json.load(f)
        return data

    