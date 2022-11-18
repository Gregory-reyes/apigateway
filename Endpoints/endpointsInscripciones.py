from flask import jsonify, request, Blueprint
from Controladores.controlInscripciones import ControladorInscripciones

controladorInscripciones = ControladorInscripciones()
endpointIncripciones = Blueprint('endpointInscripciones',__name__)

#################### PARTICIÓN DE EL MICROSERVICIO UTILIZANDO Blueprint  #################################
#endpoints para el modelo seguridad

@endpointIncripciones.route("/inscripciones",methods=['GET'])
def listar_inscripciones():
    data = request.get_json()
    response = controladorInscripciones.index()
    print (response)
    return jsonify(response)if not isinstance(response,tuple)else(jsonify(response[0]),response[1])