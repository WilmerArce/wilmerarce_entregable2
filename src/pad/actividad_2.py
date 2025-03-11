import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import seaborn as sns # necesario para estilos
import os
import sys
import json
import matplotlib
matplotlib.use("Agg") # usa un backend que no requiere interfaz grafica
import matplotlib.pyplot as plt

# configuracion inicial
np.random.seed(42)
plt.style.use('seaborn-v0_8') # nombre actualizado

#----------------------------------
# 1. Ejercicios con Arrays NumPy
#----------------------------------
# 1. Array de 10 a 29
array_10_29 = np.arange(10, 30)
print("Array 10-29:\n", array_10_29)

directorio = os.path.join("src", "pad", "static", "json") # usa os.path.join
os.makedirs(directorio, exist_ok=True)

# Ruta completa del archivo
ruta_archivo = os.path.join(directorio, "array_10_29.json") # Ruta válida

# guardar en JSON
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump({"array": array_10_29.tolist()}, archivo, indent=4)

print(f"Archivo guardado en: {ruta_archivo}")

# 2. suma de array 10x10 de unos
array_10x10 = np.ones((10, 10))
suma_10x10 = array_10x10.sum()
print("\nsuma de 10x10 de unos:", suma_10x10)
directorio = os.path.join("src", "pad", "static", "json") # usa os.path.join
os.makedirs(directorio, exist_ok=True)

# Ruta completa del archivo
ruta_archivo = os.path.join(directorio, "array_10x10.json") # Ruta válida

# Guardar en JSON
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump({"array": (array_10x10).tolist()}, archivo, indent=4)

print(f"Archivo guardado en: {ruta_archivo}")

# 3. Producto elemento a elemento de dos arrays
arr1 = np.random.randint(1, 11, 5)
arr2 = np.random.randint(1, 11, 5)
producto = arr1 * arr2
print("\nProducto elemento a elemento:\n", arr1, "*", arr2, "=", producto)

directorio = os.path.join("src", "pad", "static", "json") # Usa os.path.join
os.makedirs(directorio, exist_ok=True)

ruta_archivo = os.path.join(directorio, "producto_array.json")

# Guardar en un archivo JSON
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump({"arr1": arr1.tolist(), "arr2": arr2.tolist(), "producto": producto.tolist()}, archivo, indent=4)

print(f"Archivo guardado en: {ruta_archivo}")

# 4. Matriz 4x4 invertible (i*2 + j)
matriz_4x4 = np.fromfunction(lambda i, j: i*2 + j, (4,4), dtype=int) # Matriz invertible
inversa_4x4 = np.linalg.inv(matriz_4x4)
print("\nMatriz 4x4 (i*2 + j):\n", matriz_4x4)
print("\nInversa:\n", inversa_4x4)
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # crear directorio si no existe

# Ruta del archivo JSON
ruta_archivo = os.path.join(directorio, "matriz_inversa.json")

# Guardar en JSON (convertimos a listas)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "matriz_4x4": matriz_4x4.tolist(),
            "inversa_4x4": inversa_4x4.tolist() if inversa_4x4 is not None else "No tiene inversa"
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# 5. Máximo y mínimo con índices
array_100 = np.random.rand(100)
maximo, minimo = array_100.max(), array_100.min()
idx_max, idx_min = array_100.argmax(), array_100.argmin()
print(f"\nMaximo: {maximo: .3f} (índice {idx_max})")
print(f"\nMinimo: {minimo: .3f} (índice {idx_min})")
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta del archivo JSON
ruta_archivo = os.path.join(directorio, "array_100.json")

# Guardar en JSON (convertimos a lista y valores flotantes)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "array_100": array_100.tolist(), # convertir array a lista
            "maximo": float(maximo),
            "indice_maximo": int(idx_max),
            "minimo": float(minimo),
            "indice_minimo": int(idx_min)
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# 6. Broadcasting 3x1 + 1x3 (explicito)
a = np.array([2, 3, 4]) # columna 3x1 (valores 2, 3, 4)
b = np.array([[4, 5, 6]]) # fila 1x3
resultado = a + b # broadcasting a 3x3
print("\nResultado Broadcasting:\n", resultado)
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta de archivo JSON
ruta_archivo = os.path.join(directorio, "broadcasting.json")

# Guardar en JSON (convertimos a listas)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "a": a.tolist(), # convertir a lista
            "b": b.tolist(),
            "resultado": resultado.tolist()
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# 7. Submatriz 2x2 desde fila 2, columna 2 (índices 1)
matriz_5x5 = np.random.randint(1, 10, (5,5))
submatriz = matriz_5x5[1:3, 1:3]
print("\nSubmatriz 2x2:\n", submatriz)
# Definir directorio para guardar en JSON
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta del archivo JSON
ruta_archivo = os.path.join(directorio, "matriz_submatriz.json")

# Guardar en JSON (convertimos a listas)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "matriz_5x5": matriz_5x5.tolist(),
            "submatriz_2x2": submatriz.tolist()
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# 8. Array de ceros modificado
zeros_mod = np.zeros(10)
zeros_mod[3:7] = 5
print("\nArray de ceros modificado:\n", zeros_mod)
# Definir directorio para guardar en JSON
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta de archivo JSON
ruta_archivo = os.path.join(directorio, "array_zeros_mod.json")

# Guardar en JSON (convertimos a lista)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump({"zeros_mod": zeros_mod.tolist()}, archivo, indent=4)

print(f"Archivo guardado en: {ruta_archivo}")


# 9. Invertir filas de matriz 3x3
matriz_3x3 = np.array([[1,2,3], [4,5,6], [7,8,9]])
matriz_invertida = matriz_3x3[::-1]
print("\nMatriz invertida:\n", matriz_invertida)
# Definir directorio para guardar en JSON
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta del archivo JSON
ruta_archivo = os.path.join(directorio, "matriz_invertida.json")

# Guardar en JSON (convertimos a listas)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "matriz_3x3": matriz_3x3.tolist(),
            "matriz_invertida": matriz_invertida.tolist()
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# 10. Seleccionar elementos >0.5
arr_rand = np.random.rand(10)
selected = arr_rand[arr_rand > 0.5]
print("\nElementos >0.5:\n", selected)
# Definir directorio para guardar en JSON
directorio = os.path.join("src", "pad", "static", "json")
os.makedirs(directorio, exist_ok=True) # Crear carpeta si no existe

# Ruta del archivo JSON
ruta_archivo = os.path.join(directorio, "valores_mayores_0.5.json")

# Guardar en JSON (convertimos a listas)
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump(
        {
            "array_completo": arr_rand.tolist(),
            "mayores_a_0.5": selected.tolist()
        },
        archivo,
        indent=4
    )

print(f"Archivo guardado en: {ruta_archivo}")

# ----------------------------------
# 2. Gráficos de dispersión/Densidad
# ----------------------------------
# 11. Scatter plot básico
plt.figure(figsize=(10, 6))
x1, y1 = np.random.rand(100), np.random.rand(100)
plt.scatter(x1, y1, alpha=0.7, edgecolors='k')
plt.title("Gráfico de Dispersión Aleatorio")
plt.xlabel("x"), plt.ylabel("y")
print("x1:", x1)
print("y1:", y1)
plt.savefig("graficas_generadas1.jpg", dpi=300) # Alta resolución

# 12. Scatter plot con y = sin(x) + ruido
plt.figure(figsize=(10, 6))
x2 = np.linspace(-2*np.pi, 2*np.pi, 100)
y2 = np.sin(x2) + np.random.normal(0, 0.2, 100)
plt.scatter(x2, y2, label=r"$y = \sin(x) + \mathcal{N}(0,0.2)$")
plt.plot(x2, np.sin(x2), color='red', linewidth=2, label=r"$y = \sin(x)$")
plt.title("Función Seno con Ruido Gaussiano")
plt.legend()
print("x2:", x2)
print("y2:", y2)
plt.savefig("graficas_generadas2.jpg", dpi=300) # Alta resolución

# 13. Gráfico de contorno con meshgrid
plt.figure(figsize=(10, 6))
x3 = np.linspace(-5, 5, 100)
y3 = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x3, y3)
Z = np.cos(X) + np.sin(Y)
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.title(r"Gráfico de Contorno: $z = \cos(x) + \sin(y)$")
print("x3:", x3)
print("y3:", y3)
print("X:", X)
print("Y:", Y)
print("Z:", Z)
plt.savefig("graficas_generadas3.jpg", dpi=300) # Alta resolución

