from docxtpl import DocxTemplate
import  time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from os import getcwd

def enviarCorreo(path_name, file_name,direccioDeCorreo):

    # Para configurar gmail y poder enviar correos hay que setear 2 verification y crear una custom app en la cuenta de google
    # Iniciamos los parámetros del script
    remitente = "bolivariano.automated@gmail.com"
    my_pass = "rnguutslnoexyetr"
    destinatarios = direccioDeCorreo
    asunto = '[RPI] Correo de prueba'
    cuerpo = 'Este es el contenido del mensaje'
    ruta_adjunto = path_name
    nombre_adjunto = file_name
    print(direccioDeCorreo)
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

def generarPdf(contenido,templateName):
    switch(templateName=templateName,contenido=contenido)

    

    


def switch(templateName,contenido):
    if templateName == "Prosecucion":
        doc = DocxTemplate(f"Inputs/Templates/{templateName}.docx")

        doc.render(contenido)
        doc.save(contenido['nombreEstudiante']+".docx")
    
        time.sleep(3)
        path_docx = f"{contenido['nombreEstudiante']}.docx"
        nombre_docx = f"{contenido['nombreEstudiante']}.docx"
        enviarCorreo(path_docx,nombre_docx,contenido['correo'])
        return nombre_docx
        
    elif templateName == "constanciaTrabajo":
        print("Generando Trabajo")
        doc = DocxTemplate(f"Inputs/Templates/{templateName}.docx")

        doc.render(contenido)
        doc.save(contenido['nombrePersona']+".docx")
        print("Generando Trabajo 2")
        time.sleep(3)
        path_docx = f"{contenido['nombrePersona']}.docx"
        nombre_docx = f"{contenido['nombrePersona']}.docx"
        print("Generando Trabajo 3")
        enviarCorreo(path_docx,nombre_docx,contenido['correo'])
        return nombre_docx
    



    
