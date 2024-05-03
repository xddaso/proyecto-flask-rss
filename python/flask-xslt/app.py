from flask import Flask, render_template
import logging
import requests
import lxml.etree as ET

app = Flask(__name__)

# mostro missatges de log de nivell INFO o superior
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template("index.html")

# indicant que section és un "path" es capturen valors com /lavanguardia/local/barcelona
@app.route("/lavanguardia/<path:section>")
def lavanguardia(section:str):
    app.logger.info(f"GENERANT 'LA VANGUARDIA': {section}")

    # ruta on es el XLST
    xslt_path = __get_xlst_path("lavanguardia.xslt")

    # URL de l'XML (https://www.lavanguardia.com/rss)
    xml_url = "https://www.lavanguardia.com/rss/" + section + ".xml"
    
    # Es genera l'HTML al servidor
    html = __transform(xslt_path = xslt_path, xml_url = xml_url)

    # Es retorna l'HTML al navegador
    return html

@app.route("/elpuntavui/<path:section>")
def elpuntavui(section:str):
    app.logger.info(f"GENERANT 'EL PUNT AVUI': {section}")

    return "Pendent d'implementar"

#
# Retorna el path complert del fitxer XLST
#
def __get_xlst_path(file_name):
    return app.root_path + "/xslt/" + file_name

# 
# Descarrega l'XML i genera l'HTML a partir del XSLT
#
def __transform(xslt_path:str, xml_url:str):
    app.logger.info(f"xslt_path = {xslt_path}")
    app.logger.info(f"xml_url = {xml_url}")

    # parsejo l'XSLT
    xslt = ET.parse(xslt_path)
    
    # creo el transformador que aplicaré als XML
    xslt_transform = ET.XSLT(xslt)
    
    # descarrego l'XML de la URL donada
    xml_response = requests.get(xml_url)
    app.logger.info(f"Descarregat XML amb status code {xml_response.status_code}")

    # parsejo l'XML
    xml = ET.fromstring(xml_response.content)

    # aplico l'XSLT a l'XML
    html = xslt_transform(xml)
    
    # el paso a text ben bonic 
    html_str = ET.tostring(html, pretty_print=True)

    return html_str

# 
# Indica al navegador client que no faci servir la cache per aquesta aplicació 
# https://stackoverflow.com/a/34067710
# 
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
