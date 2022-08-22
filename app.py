from flask import Flask, send_from_directory,request
from Helpers.helper import generarPdf,obreros
from os import getcwd
from datetime import datetime


PATH_FILE_OUTPUT = getcwd() + "/Outputs"
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
    fechaActual = obtenerFechaActual()
    print(fechaActual)
    valores = request.get_json()
    valores["diaExpedicion"] = fechaActual["dia"]
    valores["mesExpedicion"] = fechaActual["mes"]
    valores["yearExpedicion"] = fechaActual["year"]
    for mes in  mesesDic:
        if mes == valores["mesNacimiento"]:
            valores["mesNacimiento"] = mesesDic[mes]
    print(valores["mesNacimiento"])      
    #name_file = generarPdf(valores)
    return "received"

@app.get(f"/download/<name_file>")
def download_file(name_file):
    return send_from_directory(PATH_FILE_OUTPUT,path=name_file, as_attachment=True)

@app.get(f"/trabajadores/obreros")
def obrero_data():

    return obreros()

if __name__ == '__main__':
    app.run()



