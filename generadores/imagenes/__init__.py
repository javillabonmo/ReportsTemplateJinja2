"""Listado de los generadores a importar."""
from . import g1
from .protocolos import GeneradorImagen, generar_contexto_imagen

generadores: list[GeneradorImagen] = [g1]
