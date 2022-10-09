from absdocumentfact import AbsDocumentFact
from magazine import Revista

class RevistaFactory(AbsDocumentFact):

    def crearDocumento(self,Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Revista(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)