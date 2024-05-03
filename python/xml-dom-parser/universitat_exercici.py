# Fes un programa amb python que a partir d'aquest xml construeix un
# diccionari on a partir dels nom i cognom d'una persona, tinc un llistat de les assignatures.
#
# Desprès fes que el programa et demani un assignatura i et digui el nom de les persones que estan matriculades.
#
from xml.dom import minidom

doc = minidom.parse("universitat.xml")

tag_universitat = doc.getElementsByTagName("universitat")[0]

llista_tag_persona = tag_universitat.getElementsByTagName("persona")

d = {}
for tag_persona in llista_tag_persona:
    nom_alumne = tag_persona.getElementsByTagName("nom")[0].firstChild.data
    cognoms_alumne = tag_persona.getElementsByTagName("cognoms")[0].firstChild.data
    tag_assignatures = tag_persona.getElementsByTagName("assignatures")[0]

    llista_tag_assignatura = tag_assignatures.getElementsByTagName("assignatura")
    l = []
    for (tag_assignatura) in llista_tag_assignatura:
        l.append(tag_assignatura.firstChild.data)

    d[nom_alumne + " " + cognoms_alumne] = l

# Donana una persona, la llista de les seves assignatures
print("Assignatures de la persona")
nom = input("Nom --------------- ")
cognom = input("Cognom ---------- ")

nom_complert = nom + " " + cognom

print("Resultat de la cerca: ")
for assignatura in d[nom_complert]:
    print (assignatura)


