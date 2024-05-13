# Proyecto Flask Rss  
<br>

## Código Base

En el proyecto partimos de un código base que se encuentra en el siguiente enlace [Link](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fjmirinformatica%2F1asixdaw-m04%2Ftree%2Fmain%2Fpython%2Fflask-rss) comprimido en un **zip**.

<br>

## Git y GitHub

Una vez descomprimido el *zip* procedemos a inicializar un repositorio `Git` en la carpeta base del proyecto:

<br>

Nos dirigimos a la carpeta raíz del proyecto:

```bash
cd ruta_raiz_proyecto
```
<br>

Inicializamos un repositorio vacío:

```bash
git init
```
<br>

### Creación de un repositorio en GitHub:

<br>

Si seleccionamos nuestra foto de perfil arriba a la derecha, nos saldrá el siguiente desplegable, dentro de el seleccionamos la siguiente opción:  

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/33d5e30d-1603-4151-8ad4-f25e34f5e6ee)

<br>

Una vez dentro seleccionamos la siguiente opcion:

<br>

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/bfed2159-6646-4962-872d-49f79f3fffca)

<br>

Ahora comenzamos con la configuración del repositorio:

<br>

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/d483ba02-ff74-42e6-b75a-865f75cfb40f)


> [!NOTE] 
> Ya que partimos de un código en local que posee un README.md no es necesario agregarlo en la creación del repositorio. Simplemente agregamos un nombre, descripción (opcional) y decidimos si será publico o privado, las demás opciones en principio no nos interesan, al menos por el momento.

En este caso ya había creado previamente el repositorio, este paso es solo para documentar el proceso de creación.

<br>

### Unificación de repositorios

<br>

Ahora que tenemos el repositorio en GitHub procedemos a unificarlo con nuestro repositorio local:

<br>

1. Previo a esto deberemos obtener nuestro enlace de clonación del repositorio, en este caso lo haré mediante el método HTTPS:

<br>

2. Para obtenerlo nos dirigimos a nuestro repositorio en GitHub y en el apartado de código podremos obtener el enlace:

    ![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/c154db6a-b9d2-4f50-81d1-f4610253d6fa)

<br>

3. Ahora desde la carpeta en local donde inicializamos el repositorio utilizamos el siguiente commando para enlazar ambos repos: 

    ```bash
    git remote add origin https://github.com/xddaso/proyecto-flask-rss.git
    ```
<br>

En este punto ambos repositorios estan conectados, ahora falta subir el contendio del local al remoto mediante:

```bash
git push origin main
```

> [!WARNING]
> Puede que la rama por defecto creada al iniciar iniciar el proyecto no sea main, en mi caso mediante `git branch -m main` renombré la rama de master a main

<br>

## Entornos virtuales


Para crear y configurar un un entorno virtual en este caso en Linux hay que seguir los siguientes pasos:  
<br>

1. Para crear el entorno virtual, mediante terminal en la carpeta base del proyecto introducimos:
   
   ```bash
   python3 -m venv .venv
   ```
2. Ahora que ya lo hemos creado, para activarlo introducimos:
   
   ```bash
   source .venv/bin/activate
   ```
3. En este punto nos encontramos en el entorno virtual, ahora debemos instalar los paquetes que tenemos en el archivo requeriments.txt que obtuvimos del codigo base mediante:

   ```bash
   pip install -r requirements.txt
   ```
4. Si queremos salir del entorno virutal ejecutamos:

   ```bash
   deactivate
   ```
<br>

### Flask

Para iniciar nuestra aplicación Flask dentro del entorno virtual deberemos ejecutar la siguiente linea:

```bash
flask run --debug
```
> [!IMPORTANT]
> Al iniciar la aplicación de forma local, podremos acceder a ella a traves del navegador en el enlace `http://127.0.0.1:5000` o `localhost:5000`

## RSS

En este caso nos piden incluir 2 nuevas secciones rss del diario de la vanguardia, para hacerlo creamos 2 archivos `.xml` en la siguiente ruta del proyecto:

`carpeta_raiz/rss/lavanguardia`

<br>

A continuación seleccionamos las secciones a añadir y obtenemos los rss de las mismas desde la página oficial de la vanguardia: [Link rss](https://www.lavanguardia.com/rss)

Si nos dirigimos al enlace, veríamos algo así con todas las secciones:

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/5ab0f2c9-0ce5-4df5-9d33-0fa275029b7a)

Al seleccionar una, nos redirige a una pestaña con su codigo rss que se vería algo así:

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/9a3c487d-18c1-4812-913b-2cbaf9a3776e)

En mi caso añadí las secciones de Tecnología y Comer, una vez obtenido su código rss de la web lo incluimos en los archivos `.xml` creados anteriormente:

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/7c0ec68c-f209-4195-97f0-c97dd84ce738)

<br>

## `index.html`

En la página principal debemos agregar los enlaces a las secciones agregadas, partiendo de los agregados en el codigo base, quedaría de la siguiente manera:

![image](https://github.com/xddaso/proyecto-flask-rss/assets/104591247/af848f02-46fa-44da-8e0c-94695e4eb045)

<br>

## Detalle de las entradas

Para cada item de las entradas se nos pide (descripció, dates de creació i de modificació, autor i categoria), para hacerlo debemos aplicar algunos cambios tanto en `app.py` como en `lavanguardia.html`:

### `app.py`

En este caso, debemos agregar una simple línea para mostrar los detalles que nos piden de cada seccion rss, ya que en si, las que se muestran en el archivo no son los nombres reales de cada valor de los items.

En la ruta de las secciones debemos agregar:

`print (rss.entries[0])`

Lo que quedaría de la siguiente manera en conjunto con el codigo previo:

```python
@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    rss = get_rss_lavanguardia(seccio)
    print (rss.entries[0])
    return render_template("lavanguardia.html", rss = rss)
```

### `lavanguardia.html`

Para crear una descripcion de cada entrada rss de
Descripciones para cada entrada
