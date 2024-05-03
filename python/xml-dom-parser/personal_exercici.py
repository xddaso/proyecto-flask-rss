from xml.dom import minidom

# Crear el fitxer HTML
f = open("personal.html", 'w')

f.write('<html><head><title>Personal DOM</title></head>\n')
f.write('<body>\n')

# Llegir l'arxiu XML
doc = minidom.parse("personal.xml")
tag_example = doc.documentElement
tag_people = tag_example.getElementsByTagName('people')[0]
llista_tag_person = tag_people.getElementsByTagName('person')

# Recórrer cada persona i escriure la informació a l'HTML
for tag_person in llista_tag_person:
    id = tag_person.getAttribute('id')

    tag_name = tag_person.getElementsByTagName('name')[0]
    name = tag_name.firstChild.data
    gender = tag_name.getAttribute('gender')

    age = tag_person.getElementsByTagName('age')[0].firstChild.data
    
    naixement = tag_person.getElementsByTagName('naixement')[0].firstChild.data

    f.write(f'<h2>{id} - {name}</h2>\n')
    f.write('<ul>\n')
    f.write(f'<li>age - {age}</li>\n')
    f.write(f'<li>sex - {gender}</li>\n')
    f.write(f'<li>naixement - {naixement}</li>\n')
    f.write('</ul>\n')

f.write('</body></html>')

f.close()
