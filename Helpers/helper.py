from docxtpl import DocxTemplate
import  time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


def enviarCorreo(path_name, file_name):

    # Para configurar gmail y poder enviar correos hay que setear 2 verification y crear una custom app en la cuenta de google
    # Iniciamos los parámetros del script
    remitente = "bolivariano.automated@gmail.com"
    my_pass = "rnguutslnoexyetr"
    destinatarios = "cristobalnegocio@gmail.com"
    asunto = '[RPI] Correo de prueba'
    cuerpo = 'Este es el contenido del mensaje'
    ruta_adjunto = path_name
    nombre_adjunto = file_name

    em = MIMEMultipart()
    em['From'] = remitente
    em['To'] = destinatarios
    em['Subject'] = asunto
    em.add_header('Content-Disposition', 'attachment', filename='bud.gif')

    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    em.attach(MIMEText(cuerpo, 'plain'))

    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')

    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    em.attach(adjunto_MIME)

    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login(remitente, my_pass)

    # Convertimos el objeto mensaje a texto
    texto = em.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)

    # Cerramos la conexión
    sesion_smtp.quit()

def generarPdf(contenido):
    print("Good 1")
    doc = DocxTemplate("Inputs/Templates/Prosecucion.docx")
    print("Good 2")
    doc.render(contenido)
    doc.save(f"{contenido['nombreEstudiante']}.docx")
    print("Good 3")
    time.sleep(3)
    path_docx = f"{contenido['nombreEstudiante']}.docx"
    nombre_docx = f"{contenido['nombreEstudiante']}.docx"
    #enviarCorreo(path_docx,nombre_docx)
    return nombre_docx

def obreros():
    obreros = pd.read_csv("Inputs/Trabajadores/PersonalParaCuadraturaObreros.csv")

    print(obreros["APELLIDOS Y NOMBRES"])
    apellidos_y_nombres = obreros["EDAD"]
    print(apellidos_y_nombres)
    return apellidos_y_nombres