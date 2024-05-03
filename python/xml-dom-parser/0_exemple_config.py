# Exemple de com llegir xml i imprimir nom de l'element arrel
from xml.dom import minidom

# parse() - Retorna un objecte tipus Document
# A doc guardo l'arbre DOM que representa el fitxer xml
doc = minidom.parse("config.xml");

# Amb Document.documentElement recuperem objecte que representa l'element arrel del document
tag_principal = doc.documentElement;

# tot el nom de tag amb namespace
print (f"TAGNAME de l'element arrel és {tag_principal.tagName}\n")

# nom sense namespace
print (f"LOCALNAME de l'element arrel és {tag_principal.localName}\n")

# com locaname però mes "generic"... a un XML hi ha elements que són tags i d'altres que no
# https://phuoc.ng/collection/this-vs-that/node-name-vs-tag-name/
print (f"NODENAME nom de l'element arrel és {tag_principal.nodeName}\n")

# RESUMINT:
#   NODENAME és el més genèric
#   TAGNAME és el nom del tag amb namespace (si el tingués)
#   LOCALNAME és el nom del tag sense namespace
