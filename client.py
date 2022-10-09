from absdocumentfact import AbsDocumentFact
from enums import *
from magazinefact import RevistaFactory
def Cliente(factory: AbsDocumentFact):

    factory_product = factory.crearDocumento(2001,["Juan Perez"],"LAPORTE",format.digital,["Español"],"NOSE",192,"Fundamento Algoritmo")

    return factory_product

datos_1 = {'Anno': 2001,
"Autores": ['Juan Daniel','Gian Valdiris'],
"Edicion": "LAPORTE","Idiomas":["Español"],
"Isbn":"NOSE",
"Paginas": 500,
"Titulo":"Cincuenta algoritmos profesionales", 
"format": [format.audio, format.digital]}

