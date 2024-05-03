from xml.sax import parse
from xml.sax.handler import ContentHandler

class SaxParser(ContentHandler):

    def startElement(self, name, attrs):
        print(f"START: {name}")

    def endElement(self, name):
        print(f"END: {name}")

    def characters(self, content):
        contingut_sense_espais = content.strip()
        if contingut_sense_espais != "": # no mostro els espais en blanc innecessaris
            print(f"CONTINGUT: {content}")

parse("config.xml", SaxParser())