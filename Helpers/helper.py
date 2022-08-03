from docxtpl import DocxTemplate
import  time


def generarPdf(contenido):
    doc = DocxTemplate("Inputs/Templates/Prosecucion.docx")
    doc.render(contenido)
    doc.save(f"Outputs/{contenido['nombreEstudiante']}.docx")
    time.sleep(3)
    docx = f"Outputs/{contenido['nombreEstudiante']}.docx"
    return f"{contenido['nombreEstudiante']}.docx"