from absdocumentfact import AbsDocumentFact
from enums import *
from magazinefact import RevistaFactory
def Cliente(factory: AbsDocumentFact):

    factory_product = factory.crearDocumento(2001,["Gabriel Garcia Marquez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")

    return factory_product

