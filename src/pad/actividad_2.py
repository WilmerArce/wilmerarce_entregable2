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
