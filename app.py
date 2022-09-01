import json
import mimetypes
from urllib import response
from flask import Flask, send_from_directory,jsonify,Response,request
import requests
from Helpers.helper import generarPdf
from os import getcwd
from datetime import datetime
import os
import pandas
from flask_pymongo import PyMongo
from bson import json_util


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

app.config["MONGO_URI"] = "mongodb+srv://crist16:torres@cluster0.rwiri.mongodb.net/escuela"
mongo = PyMongo(app)




@app.route('/')
def hello_world(): 
    
   
    return "Hello world"
    
    

def ProcesarFechaActual(request_data, fechaActual):
   
    request_data["diaExpedicion"] = fechaActual["dia"]
    request_data["mesExpedicion"] = fechaActual["mes"]
    request_data["yearExpedicion"] = fechaActual["year"]
    
    if "mesNacimiento" in request_data:
        print("Procesando Fecha Actual")
        for mes in  mesesDic:
            if mes == request_data["mesNacimiento"]:
                request_data["mesNacimiento"] = mesesDic[mes]
    else: 
        print("No existe el campo mesNacimiento ")

def ObtenerDatosPost():
    request_data = request.data
    
   
    request_data = json.loads(request_data.decode('utf-8'))
 
    return request_data

@app.post(f"/constancia/prosecucion")
def exportarProsecucion():
    #request_data = request.data
    #request_data = json.loads(request_data.decode('utf-8'))
    try:
        #request_data = request.json
        request_data = ObtenerDatosPost()
        fechaActual = obtenerFechaActual()    
        ProcesarFechaActual(request_data, fechaActual)         
        generarPdf(request_data,"Prosecucion")
        return "received"
    except:
        return "No se pudo procesar la información pruebe su conexion a internet o el correo destinatario"



@app.get(f"/download/prosecucion/<name_file>")
def download_file(name_file):
    try:
        return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)
    except: 
        print("no se pudo procesar")
        return "Imposible procesar"

@app.get(f"/download/constancia/<name_file>")
def download_constancia(name_file):
    try:
        return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)
    except: 
        print("no se pudo procesar")
        return "Imposible procesar"



@app.post(f"/constancia/constanciaTrabajo")
def exportarConstanciaDeTrabajo():
    print("Executed")
    try:
        request_data = ObtenerDatosPost()     
        print(request_data)
        fechaActual = obtenerFechaActual()
        print(fechaActual)
        ProcesarFechaActual(request_data=request_data,fechaActual=fechaActual)
        generarPdf(contenido=request_data,templateName="constanciaTrabajo")
        return f'Constancia Enviada al correo {request_data["correo"]}'
    except: 
        return "No se pudo procesar la información pruebe su conexion a internet o el correo destinatario"

@app.get(f"/trabajadores")
def getTrabajadores():
    trabajadoresBson = mongo.db.Trabajadores.find()
    response = json_util.dumps(trabajadoresBson)
    print(response)
    return Response(response, mimetype="application/json")

if __name__ == '__main__':
    app.run()
    
    
    

