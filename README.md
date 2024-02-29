# txt2gift

El presente script **txt2gift.py** ha sido realizado para facilitar la creación de lotes de preguntas en [formato GIFT](https://docs.moodle.org/all/es/Formato_GIFT) aceptado por cualquier Moodle para cargar baterías de preguntas. 

El script tiene como entrada un simple fichero de texto plano en el formato explicado más abajo y tiene como salida un fichero GIFT que podremos importar en Moodle sin problemas. 
Dicho fichero de entrada .txt se puede editar con Notepad o cualquier otro editor de texto plano o sin formato.

En principio el script está pensado solo para preguntas de opción múltiple donde solo hay una respuesta válida. La penalización de las respuestas incorrectas está fijada a -33.3% pero se puede cambiar en el código editanto el script como veremos más adelante. 

## Utilización del comando:

Es necesario tener instalado Python en tu equipo para su ejecución:
[Descarga Python](https://www.python.org/downloads/)

Tendremos que ejecutar en el terminal, en el directorio donde se encuentre el script y el fichero txt de entrada, el siguiente comando:
```
python txt2gift.py input_questions.txt test_name
```

Donde: 

- **input_questions.txt** es un fichero de texto plano de entrada. Tendrá un formato determinado (explicado en el siguiente punto).
- **test_name** es el nombre que le daremos al test (sin espacios). Se utilizará dicho nombre para nombrar las preguntas dentro del fichero y también para nombrar el fichero de salida. 

Una vez ejecutado, obtendremos un fichero llamado `test_name_gift.txt` que será el que tendremos que importar en Moodle.

## Formato de fichero de texto de entrada.
Como se puede observar en el fichero de ejemplo de entrada **example_input_questions.txt** este fichero contendrá las preguntas. Cada pregunta y sus respuestas se escriben en líneas consecutivas. El enunciado de la pregunta será la primera línea y el resto de líneas son las posibles respuestas. La respuesta marcada con asterisco (*), será la válida.
Cada pregunta y sus opciones se separarán con doble salto de línea del siguiente grupo de pregunta con respuestas.
Ejemplo:
```
Enunciado de la pregunta 1:
*Respuesta correcta
Respuesta incorrecta
Respuesta incorrecta
Respuesta incorrecta

Enunciado de la pregunta 2:
Respuesta incorrecta
*Respuesta correcta
Respuesta incorrecta
Respuesta incorrecta
```

## Importar fichero GIFT en Moodle

Seguir los siguentes pasos para importar el GIFT:

- Crear Cuestionario de Moodle
- Ir a la sección **Banco de preguntas**
- En el desplegable que pone **Preguntas** le damos a **Importar**
- En **Formato de Archivo** marcamos la opción **Formato GIFT**
- Le damos a Seleccionar Archivo > Subir un archivo. Seleccionamos el fichero `test_name_gift.txt` generado por el script. 
- Le damos a **Subir este archivo**
- Finalmente le damos a **Importar**

Y listo ya tendremos esta batería de preguntas en el bando de preguntas. Cuando agreguemos preguntas al presente test o a cualquier otro, podremos darle a **+ del banco de preguntas**

## Ajuste del porcentaje de penalización

Se puede ajustar el porcentaje de penalización de las respuestas incorrectas editando la variable dentro del script en esta linea:

```python
# Porcentaje de penalización de las respuestas erróneas (por defecto -33.33333%)
# Si se desea otro, cambiar a mano esta cifra
porcentaje_incorrectas = -33.33333
```
