from flask import jsonify, request, Blueprint
from Controladores.controlSeguridad import ControladorSeguridad

controladorSeguridad = ControladorSeguridad()
endpointSeguridad = Blueprint('endpointSeguridad',__name__)

#################### PARTICIÓN DE EL MICROSERVICIO UTILIZANDO Blueprint  #################################
#endpoints para el modelo seguridad

@endpointSeguridad.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    response = controladorSeguridad.login(data)
    return response
