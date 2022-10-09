from abc import ABC, abstractmethod
from typing import List
from enums import format, category
class Documentos(ABC):
    __Anno: int
    __Autores: List[str]
    __Edicion: str
    __format: List[format]
    __Idiomas: List[str]
    __isbn: str
    __paginas: int
    __titulo: str
    __Categoria: category

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, format: List[format], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        
        self.__Anno = Anno
        self.__Autores = Autores
        self.__Edicion = Edicion
        self.__format= format
        self.__Idiomas= Idiomas
        self.__isbn= Isbn
        self.__paginas= Paginas
        self.__titulo= Titulo
        
    
    def Documentos(self):
        pass
    
    def categoria(self, categoria):
        self.__Categoria= categoria
        
    
    def getCategoria(self):
        return self.__Categoria
        
