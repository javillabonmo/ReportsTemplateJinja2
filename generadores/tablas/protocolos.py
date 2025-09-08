"""Colección del protocolo que describe los componentes mínimos de la integración."""
from typing import Protocol, Union

from pandas.core.frame import DataFrame as Dataframe


class GeneradorTabla(Protocol):
    """
    Módulo que contiene la configuración del script generador de las tablas.

    Attributes
    ----------
    ID
        identificador (va a ser utilizado para guardar la tabla en el contexto) y  para inyectarlo en el cuerpo del documento.
    """

    def generar_tabla(self, df: Dataframe) -> dict[str, Union[list[str]]]:
        """
        Genera una tabla a partir de un dataframe de pandas.

        La descripción de cada imagen estará en el módulo de su implementación.

        Returns
        -------
        list[dict]
            Contexto de la tala generada
        """
        pass

    id: str
