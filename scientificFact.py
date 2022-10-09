from absdocumentfact import AbsDocumentFact
from scientific import Cientifico

class CientificoFactory(AbsDocumentFact):

    def crearDocumento(self, Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Cientifico(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)