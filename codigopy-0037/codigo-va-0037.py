# Angela Correa NC = 0037
import cv2
from pathlib import Path

carpeta_script = Path(__file__).resolve().parent
carpeta_proyecto = carpeta_script.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-0037"
    / "img-toyota-0037.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0037"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)
# Impresiones de depuración
print("Directorio de trabajo actual:", carpeta_proyecto.absolute())
print("Buscando la imagen en:", ruta_original.absolute())
print("¿El archivo existe?:", ruta_original.exists())

img0037 = cv2.imread(str(ruta_original))

if img0037 is None:
    print("\n--- CONTENIDO DEL DIRECTORIO ACTUAL ---")
    for elemento in carpeta_proyecto.iterdir():
        print(" -", elemento.name)
    raise FileNotFoundError(
        f"No se pudo encontrar o leer la imagen en: {ruta_original.absolute()}"
    )
# 3. Rotar la imagen 90 grados en sentido horario
img90_0037 = cv2.rotate(
    img0037, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0037.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0037 = cv2.warpAffine(
    img0037,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0037 = cv2.resize(
    img0037, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0037 = img0037.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0037,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("toyota original 0037", img0037)

cv2.imshow("toyota 90 0037", img90_0037)

cv2.imshow("toyota 45 0037", img45_0037)

cv2.imshow(
    "toyota 600x500 0037",
    img600x500_0037
)

cv2.imshow("toyota rojo 0037", img_rojo_0037)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-toyota1-0037.jpg"),
    img90_0037
)

cv2.imwrite(
    str(carpeta_resultados / "img-toyota2-0037.jpg"),
    img45_0037
)

cv2.imwrite(
    str(carpeta_resultados / "img-toyota3-0037.jpg"),
    img600x500_0037
)

cv2.imwrite(
    str(carpeta_resultados / "img-toyota4-0037.jpg"),
    img_rojo_0037
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()
print("Angela Correa NC = 0037")