from absdocumentfact import AbsDocumentFact
from book import Libro

class LibroFactory(AbsDocumentFact):

    def crearDocumento(self, Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Libro(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)