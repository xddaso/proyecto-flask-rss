from xml.dom import minidom 

doc = minidom.parse("diaris.xml")

tag_principal = doc.documentElement

print("<html><head><title>Diaris DOM</title></head><body>")

llista_tag_diari = tag_principal.getElementsByTagName("diari")
for tag_diari in llista_tag_diari:
    id = tag_diari.getAttribute("id")
    nom = tag_diari.getElementsByTagName("nom")[0].firstChild.data
    url = tag_diari.getElementsByTagName("url")[0].firstChild.data
    
    print("<p>")
    print(f"<a id='{id}' href='{url}'>#{id} {nom}</a>")
    print("</p>")

print("</body></html>")
