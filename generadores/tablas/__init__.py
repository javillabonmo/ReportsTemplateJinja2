"""Listado de los generadores a importar."""

from . import g1
from .protocolos import GeneradorTabla

generadores: list[GeneradorTabla] = [g1]