from document import Documentos
from InterMulti import IOnline

from enums import format, category
from typing import List
class Cientifico(Documentos, IOnline):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, format: List[format], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, format, Idiomas, Isbn,Paginas,Titulo)

    