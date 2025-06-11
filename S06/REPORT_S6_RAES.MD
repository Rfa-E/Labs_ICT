# Deliverable Session 06 – Information and Communication Technology

## Rafael Antonio Echevarria Silva

In this session, we’ll build a simple web-based user interface for our RESTful services using HTML, CSS, forms and Flask templating.

### Ex. 1: Basic HTML page

En este primer ejercicio creamos un fichero **.html** con la estructura mínima de cualquier página web estática:

- Declaración de tipo y etiquetas <html>, <head> y <body>.
- Un <title> para el nombre de la pestaña.
- Un encabezado (<h1>) con un texto representativo.
- Uno o varios párrafos (<p>).
- Una imagen (<img>) con ruta relativa dentro de **static/**.

La ubicación de los ficheros ha de seguir el patrón de Flask:

- Plantillas HTML en **templates/**.
- Recursos estáticos (imágenes, CSS) en **static/**.

### Ex. 2: Home con plantilla y parámetro “group”

Creamos un endpoint ('/') en Flask que:

1. Lee el parámetro GET **group** de la URL.
2. Lo pasa al **render_template()** junto al título y encabezado.
3. En la plantilla, usamos Jinja para insertar **{{ group }}** en <title> y <h1>.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('group')
    return render_template('hello.html', name = name)
```

La plantilla hello.html mostrará dinámicamente el nombre de tu grupo.

### Ex. 3: Listado de sensores desde la base de datos

Definimos un nuevo endpoint ('/sensors') que:

1. Conecta a la base de datos SQLite.
2. Ejecuta **SELECT * FROM sensors**.
3. Recupera la lista de sensores.
4. Pasa el resultado al template **info.html**.

En el template:

- Construimos una tabla <table> con <thead> para los encabezados de columnas y <tbody> para cada fila de sensor.
- Iteramos sobre la lista con Jinja:

```html
<table>
            <thead>
                <tr>
                    {% for col in columns %}
                        <th>{{ col }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in data %}
                    <tr>
                        {% for col in columns %}
                            <td>{{ row[col] }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
```

### Ex. 4: Navegación y estilos CSS

En este apartado mejoramos la usabilidad y apariencia:

1. **Enlaces de navegación**
   - Añadimos <a href="/">Home</a> en cada plantilla.
   - Añadimos <a href="/info">Info</a> o al revés según corresponda, para permitir saltar entre páginas.
2. **Hoja de estilos**
   - Creamos static/style.css con reglas CSS a gusto (colores, márgenes, fuentes).
   - En cada plantilla incluimos:

    ```html
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    ```

3. **Estilos dinámicos**
Pregunta extra:
Se podría cambiar el estilo (por ejemplo, color de fondo) inyectando en la plantilla una variable de estado del sensor y usando clases CSS distintas según el valor actual del sensor.

### Ex. 5: Formulario HTML y endpoint /showtext

Utilizamos formularios HTML para enviar datos al servidor:

1. **Formulario en plantilla**

    ```html
    <h2>Send a Message to the API</h2>
        <form action="/showtext" method="POST">
            <label for="usertext">Enter your text:</label><br>
            <input type="text" id="usertext" name="usertext" required>
            <input type="submit" value="Submit">
        </form>
    ```

2. **Endpoint en Flask**

    ```python
    @app.route('/showtext', methods=['POST'])
    def showtext():
        user_input = request.form.get('usertext')
        rand = random_colour()
        sense.show_message(user_input, text_colour = rand, back_colour = (0,0,0))
        return render_template('main.html')
    #     print(f"Received text from form: {user_input}")
    #     return f"<h1>You sent: {user_input}</h1><p>Check the server console for the printed text.</p>"
    ```

3. **Despliegue en Sense HAT**

- Podemos enviar el texto y color al LED matrix con **sense.show_message()**.
- Se añade un segundo input para elegir el color y se procesa en la función.
