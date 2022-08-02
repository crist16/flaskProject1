from docxtpl import DocxTemplate
import  time
content = {
    "nombreEstudiante": "Cristobal",
    "cedulaEstudiante": "19762932",
    "ciudadNacimiento": "Cumana",
    "diaNacimiento": "05-05-1991",
    "mesNacimiento": "Mayo",
    "gradoCurso": "Tercer",
    "literal": "A",
    "periodoEscolar": "2022-2023",
    "gradoPromovido": "Cuarto",
    "nivelPromovido": "Basica",
    "diaExpedicion": "13",
    "mesExpedicion": "Julio",
    "yearExpedicion": "2022"

}

def generarPdf(contenido):
    doc = DocxTemplate("Inputs/Templates/Prosecucion.docx")
    doc.render(contenido)
    doc.save(f"Outputs/{contenido['nombreEstudiante']}.docx")
    time.sleep(3)
    docx = f"Outputs/{contenido['nombreEstudiante']}.docx"
    return f"{contenido['nombreEstudiante']}.docx"