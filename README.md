# txt2gift

El presente script **txt2gift.py** ha sido realizado para facilitar la creación de lotes de preguntas en [formato GIFT](https://docs.moodle.org/all/es/Formato_GIFT) aceptado por cualquier Moodle para cargar baterías de preguntas. 

En principio está pensado solo para preguntas de opción múltiple donde solo hay una respuesta válida.

Se puede ajustar el porcentaje de penalización de las respuestas incorrectas editando la variable dentro del script en esta línea:

```python
# Porcentaje de penalización de las respuestas erróneas (por defecto -33.33333%)
# Si se desea otro, cambiar a mano esta cifra
porcentaje_incorrectas = -33.33333
```

## Utilización del comando:

Es necesario tener instalado Python en tu equipo para su ejecución:
[Descarga Python](https://www.python.org/downloads/)


Tendremos que ejecutar en el terminal en el directorio donde se encuentre el script y el fichero de entrada el siguiente comando:
```
python txt2gift.py input_questions.txt test_name
```

Donde: 

- **input_questions.txt** es un fichero de textod plano de entrada. Tendrá un formato determinado explicado en el siguiente punto.
- **test_name** es el nombre que le daremos al test. Se utilizará dicha cadena de texto para nombrar las preguntas dentro del fichero y también para nombrar el fichero de salida. 

## Formato de fichero de texto de entrada.
Como se puede observar en el fichero de ejemplo de entrada **example_input_questions.txt** este fichero contendrá las preguntas. Cada pregunta y sus respuestas se escriben en líneas consecutivas. El enunciado de la pregunta será la primera línea y el resto de líneas son las posibles respuestas. La respuesta marcada con asterisco (*), será la válida.
Cada pregunta y sus opciones se separarán con doble salto de línea. 
Ejemplo:
```
Enunciado de la pregunta 1:
*Respuesta correcta
Respuesta incorrecta
Respuesta incorrecta
Respuesta incorrecta

Enunciado de la pregunta 2:
*Respuesta correcta
Respuesta incorrecta
Respuesta incorrecta
Respuesta incorrecta
```





