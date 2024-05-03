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

    # obro el fitxer en mode escriptura
    file = open("diaris.html", "w")

    def startElement(self, name, attrs):
        if (name == "diaris"):
            self.file.write("<html><head><title>Diaris v3</title></head><body>\n")
        elif (name == "diari"):
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
            self.file.write("<p>")
            self.file.write(f"<a id='{self.currentId}' href='{self.currentUrl}'>#{self.currentId} {self.currentNom}</a>")
            self.file.write("</p>\n")
        elif (name == "diaris"):
            self.file.write("</body></html>")
            self.file.close()

    def characters(self, content):
        if self.insideNom:
            self.currentNom = content
        elif self.insideUrl:
            self.currentUrl = content

parse("diaris.xml", SaxParser())