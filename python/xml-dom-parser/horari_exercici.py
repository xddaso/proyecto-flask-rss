from xml.dom import minidom

file = open("horari.html", "w")
file.write("<html><head><title>Horari DOM</title></head><body>\n")

# Parsegem el document XML
doc = minidom.parse('horari.xml')

tag_horari = doc.documentElement

tag_alumne = tag_horari.getElementsByTagName('alumne')[0]

nom = tag_alumne.getElementsByTagName('nom')[0].firstChild.data
curs = tag_alumne.getElementsByTagName('curs')[0].firstChild.data
foto = tag_alumne.getElementsByTagName('foto')[0].firstChild.data

file.write(f"<h1>{nom}</h1>\n")
file.write(f"<h2>{curs}</h2>\n")
file.write(f"<p><img src='{foto}' alt='Foto de l'alumne' width='100' height='100'/></p>\n")
colors = {}
tag_colors = tag_horari.getElementsByTagName('colors')[0]
for tag_assignatura in tag_colors.getElementsByTagName('assignatura'):
    color = tag_assignatura.getAttribute('color')
    assignatura = tag_assignatura.firstChild.data
    colors[assignatura] = color

franges = []
tag_franges = tag_horari.getElementsByTagName('franges')[0]
for tag_franja in tag_franges.getElementsByTagName('franja'):
    franges.append(tag_franja.firstChild.data)

dies = []
classes = {}
tag_classes = tag_horari.getElementsByTagName('classes')[0]
for tag_dia in tag_classes.getElementsByTagName('dia'):
    dia = tag_dia.getElementsByTagName('nom')[0].firstChild.data

    dies.append(dia)
    classes[dia] = []

    tag_assignatures = tag_dia.getElementsByTagName('assignatures')[0]
    for tag_assignatura in tag_assignatures.getElementsByTagName('assignatura'):
        assignatura = tag_assignatura.firstChild.data
        classes[dia].append(assignatura)

file.write("<table border='1'>\n")

# Capçalera
file.write("<tr><th></th>")
for dia in dies:
    file.write(f"<th>{dia}</th>")
file.write("</tr>\n")

# Contingut
num_franges = len(franges)
for i in range(num_franges):
    file.write("<tr>\n")
    file.write(f"\t<td>{franges[i]}</td>\n")
    for dia in dies:
        assignatura = classes[dia][i]
        file.write(f"\t<td style='background-color: {colors[assignatura]}'>{assignatura}</td>\n")
    file.write("</tr>\n")

file.write("</table>\n")

file.write("</body></html>")
file.close()

print("Horari disponible en horari.html.")
