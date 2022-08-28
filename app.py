import json
from flask import Flask, send_from_directory,jsonify,request
from Helpers.helper import generarPdf,obreros
from os import getcwd
from datetime import datetime


PATH_FILE_OUTPUT = getcwd() + "/"
mesesDic = {
    "01":'ENERO',
    "02":'FEBRERO',
    "03":'MARZO',
    "04":'ABRIL',
    "05":'MAYO',
    "06":'JUNIO',
    "07":'JULIO',
    "08":'AGOSTO',
    "09":'SEPTIEMBRE',
    "10":'OCTUBRE',
    "11":'NOVIEMBRE',
    "12":'DICIEMBRE'
}

def obtenerFechaActual():
    fecha = datetime.now()
    diaHoy = fecha.strftime("%d")
    mesHoy = fecha.strftime("%m")
    yearHoy = fecha.strftime("%Y")
    fechaCompletaDeHoy = {
        "dia" : diaHoy,
        "year" : yearHoy
    }
    for mes in  mesesDic:
        if mes == mesHoy:
            fechaCompletaDeHoy["mes"] = mesesDic[mes]
    return fechaCompletaDeHoy

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World '


@app.post(f"/constancia/prosecucion")
def exportarProsecucion():
    #request_data = request.data
    #request_data = json.loads(request_data.decode('utf-8'))
    try:
        #request_data = request.json
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        fechaActual = obtenerFechaActual()
        print(fechaActual)
    
        request_data["diaExpedicion"] = fechaActual["dia"]
        request_data["mesExpedicion"] = fechaActual["mes"]
        request_data["yearExpedicion"] = fechaActual["year"]
        print(request_data)
        for mes in  mesesDic:
            if mes == request_data["mesNacimiento"]:
                request_data["mesNacimiento"] = mesesDic[mes]
         
        name_file = generarPdf(request_data)
        return "received"
    except:
        return "Hubo un error al procesar la informacion"

@app.get(f"/download/<name_file>")
def download_file(name_file):
    try:
        return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)
    except: 
        print("no se pudo procesar")
        return "Imposible procesar"

@app.get(f"/trabajadores/obreros")
def obrero_data():

    return obreros()

if __name__ == '__main__':
    app.run()



