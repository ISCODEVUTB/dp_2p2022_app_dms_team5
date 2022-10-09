from document import Documentos
from InterOnline import IOnline
from InterPdf import IPdf
from enums import format, category
from typing import List
class Cientifico(Documentos, IOnline):
      def itemOnline(self) ->str:
        return "Scientific Online Document"
    
    