from lxml import etree

# carrego en la variable xml el fitxer XML
xml = etree.parse("config.xml")

# carrego l'XSD (que també un XML) fent servir una altre llibreria
xsd_as_xml = etree.parse("config.xsd")

# creo un objecte que em permetrà validar el fitxer XML
xsd = etree.XMLSchema(xsd_as_xml)

# valido el fitxer XML
xsd.validate(xml)

# si arribo fins aquí, el fitxer XML és vàlid
print("El fitxer XML és vàlid")

# mostro el tag principal del fitxer XML
nom_tag_principal = xml.getroot().tag
print("Tag principal: ", nom_tag_principal)