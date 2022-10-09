from document import Documentos
from InterPdf import IPdf
from enums import format, category
from typing import List
class Libro(Documentos, IPdf):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, format: List[format], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, format, Idiomas, Isbn,Paginas,Titulo)

    def operaciones(self):
        return "Haciendo Operaciones!"

   

