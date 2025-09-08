"""Colección del protocolo que describe los componentes mínimos de la integración."""
from typing import Protocol

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage  # type: ignore
from pandas.core.frame import DataFrame as Dataframe


class GeneradorImagen(Protocol):
    """
    Módulo que contiene la configuración del script generador de las imágenes.

    Attributes
    ----------
    titulo
        Título (va a ser utilizado para guardar la imagen) y opcionalmente para inyectarlo en el cuerpo del documento.
    ancho_mm
        Ancho de la imagen en milímetros para formatearlo en la imagen. (puede ser 0.0 para que sea determinado automáticamente)
    alto_mm
        Alto de la imagen en milímetros para formatearlo en la imagen. (puede ser 0.0 para que sea determinado automáticamente)
    """

    def guardar_imagen(self, df: Dataframe) -> str:
        """
        Genera una imagen a partir de un dataframe de pandas.

        La descripción de cada imagen estará en el módulo de su implementación.

        Returns
        -------
        str
            Ruta a la imagen generada
        """
        pass

    descripcion: str
    titulo: str
    ancho_mm: float
    alto_mm: float
    path: str


def generar_contexto_imagen(generador: GeneradorImagen, template: DocxTemplate, df: Dataframe) -> InlineImage:
    """
    Genera el contexto de una imagen para ser usado en un plantilla de docxtpl.

    Esta función no grafica directamenta la imagen, solo genera un objeto de InlineImage
    que puede ser usado ara inyectarlo en un contexto (revisar tests/test_generadores.py)
    para entenderlo mejor.

    Parameters
    ----------
    generador
        Módulo generador de imágenes a utilizar.
    template
        Objeto de DocxTemplate donde va a ser colocada la imagen.
    df
        Dataframe con la data que recibe el generador.

    Returns
    -------
    InlineImage
        Un objeto de InlineImage que puede ser colocado en un diccionario de contexto.
    """
    alto = Mm(generador.alto_mm) if generador.alto_mm != 0.0 else None
    ancho = Mm(generador.ancho_mm) if generador.ancho_mm != 0.0 else None
    return InlineImage(template, generador.guardar_imagen(df), alto, ancho)
