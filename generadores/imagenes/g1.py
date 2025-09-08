"""Módulo de imagen del gráfico de barras del género favorito más popular."""
from pandas.core.frame import DataFrame as Dataframe
import matplotlib.pyplot as plt

titulo = "Visualización"
ancho_mm = 0.0
alto_mm = 0.0
descripcion = "Gráfico de barras del género favorito más popular"


path = "__tmp/" + titulo.replace(" ", "_").lower() + ".png"


def guardar_imagen(df: Dataframe) -> str:
    """
    Genera una imagen a partir de un dataframe de pandas.

    Imagen que tiene un gráfico de barras del género favorito más popular.

    Returns
    -------
    str
        Ruta a la imagen generada
    """
    results = df.groupby('genero_favorito').count()['nombre']

    fig, ax = plt.subplots()

    ax.bar(results.index, results, width=1, edgecolor="white", linewidth=0.7)
    fig.savefig(path)
    return path
