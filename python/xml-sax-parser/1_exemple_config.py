from xml.sax import parse
from xml.sax.handler import ContentHandler

class SaxParser(ContentHandler):

    # variables per saber si estic dins de una etiqueta
    insideNom = False
    insideEdat = False

    def startElement(self, name, attrs):
        if(name == "nom"):
            self.insideNom = True
        elif(name == "edat"):
            self.insideEdat = True

    def endElement(self, name):
        if(name == "nom"):
            self.insideNom = False
        elif(name == "edat"):
            self.insideEdat = False

    def characters(self, content):
        if self.insideNom:
            print(f"NOM: {content}")
        elif self.insideEdat:
            print(f"EDAT: {content}")

parse("config.xml", SaxParser())