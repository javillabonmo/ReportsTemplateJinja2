"""Ejemplo."""
from pandas.core.frame import DataFrame as Dataframe
from typing import Union

id = "general"


def generar_tabla(df: Dataframe) -> dict[str, Union[list[str]]]:
    """
    Genera una tabla a partir de un dataframe de pandas.

    La tabla contiene los elelmentos brutos del dataframe.

    Returns
    -------
    list[dict]
        Contexto de la tabla generada donde las llaves siempre
    """
    return {
        f"{id}_labels": [x.capitalize().replace('_', ' ') for x in df.columns.values],
        f"{id}_contents": [
            {"cols": list(x.values())}  # type: ignore
            for x in
            df.to_dict(orient="records")
        ],
    }
