"""Módulo principal, su entrada debería ser nula y su salida el documento formateado."""
import jinja2
import pandas as pd
from docxtpl import DocxTemplate  # type: ignore
from pandas.core.frame import DataFrame as Dataframe
from generadores.imagenes import generadores, generar_contexto_imagen

from generadores.tablas import (
    g1,
)
from generadores.imagenes import (
    generar_contexto_imagen,
    generadores,
)

df = Dataframe([
        {"nombre": "juan", "libros_leidos": 4, "genero_favorito": "drama"},
        {"nombre": "juano", "libros_leidos": 2, "genero_favorito": "policiaco"},
        {"nombre": "juana", "libros_leidos": 7, "genero_favorito": "drama"},
        {"nombre": "juanis", "libros_leidos": 3, "genero_favorito": "romance"},
        {"nombre": "juanito", "libros_leidos": 3, "genero_favorito": "drama"},
        {"nombre": "juanote", "libros_leidos": 12, "genero_favorito": "policiaco"},
        {"nombre": "juanete", "libros_leidos": 3, "genero_favorito": "drama"},
        {"nombre": "juanacio", "libros_leidos": 13, "genero_favorito": "drama"},
        {"nombre": "juanes", "libros_leidos": 3, "genero_favorito": "comedia"},
        {"nombre": "juanse", "libros_leidos": 5, "genero_favorito": "drama"},
    ])


tpl = DocxTemplate("templates/plantilla_imagenes.docx")

context = {
    "images": [
        {
            "title": g.titulo,
            "image": generar_contexto_imagen(g, tpl, df),
            "desc": g.descripcion,
            "path": g.path,
            "height": g.alto_mm,
            "width": g.ancho_mm,
            "id": i
        } for i, g in enumerate(generadores, 1)
    ],
}

for generador in generadores:
        context.update(g1.generar_tabla(df))

jinja_env = jinja2.Environment()
tpl.render(context, jinja_env)
tpl.save("output/reporte.docx")
