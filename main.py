import cv2
from pyzbar import pyzbar

def decode_barcodes(image_path):
    # Cargar la imagen
    img = cv2.imread(image_path)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Utilizar la biblioteca pyzbar para detectar y decodificar los códigos de barras
    barcodes = pyzbar.decode(gray)

    # Iterar sobre los códigos de barras detectados
    for barcode in barcodes:
        # Extraer las coordenadas de los vértices del código de barras y dibujar un rectángulo alrededor de él
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Decodificar el código de barras y extraer su tipo y datos
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Mostrar la información del código de barras en la imagen
        text = "{} ({})".format(barcode_data, barcode_type)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Imprimir los resultados en la consola
        print("Tipo: {}, Datos: {}".format(barcode_type, barcode_data))

    # Mostrar la imagen resultante
    cv2.imshow("Resultado", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejemplo de uso
decode_barcodes("ruta_de_la_imagen")