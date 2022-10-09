from abc import ABC , abstractmethod
from document import Documentos

class AbsDocumentFact(ABC):

    @abstractmethod
    def crearDocumento(self):
        pass

    