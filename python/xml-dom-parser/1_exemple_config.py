from xml.dom import minidom

# nom del fitxer xml de configuració
config_file = "config.xml"

# carrego en la variable doc el fitxer XML
doc = minidom.parse(config_file)

# obtinc el tag principal del fitxer XML
tag_principal = doc.documentElement

# obtinc el tag "nom" del tag principal
tag_nom = tag_principal.getElementsByTagName("nom")[0]

# obtinc el valor del tag tag_nom
nom = tag_nom.firstChild.data

# obtinc el tag "nom" del tag principal
tag_edat = tag_principal.getElementsByTagName("edat")[0]

# recupero l'edat en format int
edat = int(tag_edat.firstChild.data)

if(edat < 18):
   print(f"Hola {nom}, vols un cacaolat?")
else:
   print(f"Hola {nom}, vols una cervesa?")
