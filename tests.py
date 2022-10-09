import unittest 
from enums import *
from magazinefact import RevistaFactory
from bookfact import LibroFactory
from scientificFact import CientificoFactory
from book import Libro 
from magazine import Revista
from scientific import Cientifico
from client import Cliente
from typing import List
from document import Documentos
from enums import category
from enums import format
from absdocumentfact import AbsDocumentFact


class Tesis(Documentos):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, format: List[format], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, format, Idiomas, Isbn,Paginas,Titulo)

class TesisFactory(AbsDocumentFact):

    def crearDocumento(self, Anno, Autores, Edicion, format, Idiomas, Isbn,Paginas,Titulo):
        return Tesis(Anno, Autores, Edicion, format, Idiomas, Isbn,Paginas,Titulo)
class testFactories(unittest.TestCase):

    def test_revista_factory(self):
        magazine_one = Cliente(RevistaFactory())
        self.assertEqual(magazine_one.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(magazine_one, Revista))
    def test_tesis_factory(self):
        tesis = Cliente(TesisFactory())
        self.assertEqual(tesis.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(tesis, Tesis))
    def test_cientifico_factory(self):
        cientf = Cliente(CientificoFactory())
        self.assertEqual(cientf.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(cientf, Cientifico))
    def test_libro_factory(self):
        libro = Cliente(LibroFactory())
        self.assertEqual(libro.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(libro, Libro))
if __name__ == "__main__":
    unittest.main()   

class TestDocumentos(unittest.TestCase):
    datos_1 = {'Anno': 2001,
            "Autores": ['Gabriel Garcia Marquez','Pombo'],
            "Edicion": "LAPORTE","Idiomas":["Español"],
            "Isbn":"NOSE",
            "Paginas": 500,
            "Titulo":"Cincuenta algoritmos profesionales", 
            "format": [format.audio, format.digital]}
    
    def test_libro(self):
        book_one = Libro(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(book_one.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")

    def test_revista(self):
        magazine_one = Revista(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(magazine_one.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_tesis(self):
        tesis = Tesis(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(tesis.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_cientifico(self):
        cientf = Cientifico(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(cientf.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_setCategory(self):
        book_one = Libro(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")
        book_one.categoria(category.INGENIERIA)
        self.assertEqual(book_one.getCategoria(), category.INGENIERIA)
if __name__ == "__main__":
    unittest.main()
    
 

