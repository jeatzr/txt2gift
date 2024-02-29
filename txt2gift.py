import sys
import os

# Porcentaje de penalización de las respuestas erróneas (por defecto -33.33333%)
# Si se desea otro, cambiar a mano esta cifra
porcentaje_incorrectas = -33.33333


# Función para escapar los caracteres especiales que hay en el formato GIFT
def escape_gift(texto):
    caracteres_especiales = "~=#{}"
    for caracter in caracteres_especiales:
        texto = texto.replace(caracter, "\\" + caracter)
    return texto


# Función que genera una cadena de texto GIFT a partir e un array de preguntas de entrada
def generar_gift(preguntas, porcentaje_incorrectas, nombre_test="Test"):
    gift = ""
    for i, pregunta in enumerate(preguntas, start=1):
        enunciado = escape_gift(pregunta["enunciado"])
        opciones = pregunta["opciones"]
        opciones_gift = []
        for opcion in opciones:
            # caso de pregunta correcta
            if opcion.startswith("*"):
                opciones_gift.append("=" + escape_gift(opcion[1:]))
            # en caso de incorrecta
            else:
                opciones_gift.append(
                    "~%" + str(porcentaje_incorrectas) + "%" + escape_gift(opcion)
                )
        # Agregamos el enunciado de la pregunta al gift
        gift += "::{} - Q{}::{}".format(nombre_test, i, enunciado)
        gift += " {\n"
        # Agregamos las opciones
        for opcion in opciones_gift:
            gift += "{}\n".format(opcion)

        # fin de pregunta, separamos con doble salto de linea
        gift += "}\n\n"

    return gift


# Separa las preguntas de un archivo de texto de entrada
# definiendo cada enunciado y sus respuestas
def leer_preguntas_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    preguntas = []
    enunciado = ""
    opciones = []

    for linea in lineas:
        linea = linea.strip()
        if linea:  # Si la línea no está en blanco
            if (
                not enunciado
            ):  # Si no tenemos aún un enunciado, asumimos que esta línea es el enunciado de una nueva pregunta
                enunciado = linea
            else:  # Si ya tenemos un enunciado, asumimos que esta línea es una opción de respuesta
                opciones.append(linea)
        else:  # Si la línea está en blanco, esto marca el final de las opciones para la pregunta actual
            if (
                enunciado
            ):  # Si tenemos un enunciado, agregamos la pregunta actual a la lista de preguntas
                pregunta = {"enunciado": enunciado, "opciones": opciones}
                preguntas.append(pregunta)
                enunciado = ""
                opciones = []

    # Agregamos la última pregunta si hay alguna pendiente
    if enunciado:
        pregunta = {"enunciado": enunciado, "opciones": opciones}
        preguntas.append(pregunta)

    return preguntas


# Guarda el gift en un archivo
def guardar_gift_en_archivo(gift, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(gift)


def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py archivo_preguntas.txt Nombre_Test")
        return

    nombre_archivo_entrada = sys.argv[1]
    nombre_test = sys.argv[2]
    nombre_archivo_salida = nombre_test + "_gift.txt"

    preguntas = leer_preguntas_desde_archivo(nombre_archivo_entrada)

    gift = generar_gift(preguntas, porcentaje_incorrectas, nombre_test)

    guardar_gift_en_archivo(gift, nombre_archivo_salida)


if __name__ == "__main__":
    main()
