from xml.sax import parse
from xml.sax.handler import ContentHandler

class SaxParser(ContentHandler):

    # variables per saber si estic dins de una etiqueta
    insideNom = False
    insideUrl = False

    # variables on guardaré el contingut dels elements actuals
    currentId = None
    currentNom = None
    currentUrl = None

    def startElement(self, name, attrs):
        if (name == "diari"):
            self.currentId = attrs.get("id")
        elif (name == "nom"):
            self.insideNom = True
        elif (name == "url"):
            self.insideUrl = True

    def endElement(self, name):
        if (name == "nom"):
            self.insideNom = False
        elif (name == "url"):
            self.insideUrl = False
        elif (name == "diari"):
            # escric el contingut del diari
            print("----------------------------")
            print(f"ID: {self.currentId}")
            print(f"NOM: {self.currentNom}")
            print(f"URL: {self.currentUrl}")
            print("----------------------------")
            print()

    def characters(self, content):
        if self.insideNom:
            self.currentNom = content
        elif self.insideUrl:
            self.currentUrl = content

parse("diaris.xml", SaxParser())