import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class actividad3:
    def __init__(self, ruta_dataset):
        self.ruta_raiz = os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/pad/actividad_3/".format(self.ruta_raiz)
        datos = {
            "n_punto": [0,1,2,3,4,5,6,7,8,9,10,11],
            "detalle":["Crea un DataFrame frutas que luzca así","","","","","","","","","","",""],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],    
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object) # Convertimos a tipo de object
        print(self.ruta_raiz)

        try:
            self.review = pd.read_csv(ruta_dataset)
            print("Dataset 'Wine Reviews' cargado con exito")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_dataset}'")
            self.review = pd.DataFrame() # Inicializa un DataFrame vacio para evitar errores posteriores 
        except Exception as e: 
            print(f"Error al cargar el dataset: {e}")
            self.review = pd.DataFrame()      

    def punto_1(self):
        self.frutas = pd.DataFrame({ # Guardamos como atributo para reutilizar
            "Frutas": ["Manzana", "Banana", "Naranja", "Uva"],
            "Cantidad": [10, 15, 8, 20],
            "Precio": [0.5, 0.3, 0.6, 0.4]
        })
        self.frutas["Precio_TOTAL"] = self.frutas["Cantidad"] * self.frutas["Precio"]
        self.df.loc[0, "resultado"] = self.frutas.to_string()
        print("punto_1") 

    def punto_2(self):
        ventas_frutas = pd.DataFrame({
            "Granadilla": [20, 49],
            "Tomates": [50, 100]
        }, index=["ventas_2021", "ventas_2022"])
        self.df.loc[1, "detalle"] = "Ventas de frutas"
        self.df.loc[1, "resultado"] = ventas_frutas.to_string()
        print("punto_2") 

    def punto_3(self):
        utensilios = pd.Series({
            'CUCHARAS': 3,
            'TENEDORES': 2,
            'CUCHILLOS': 4,
            'PLATO': 5
        }, index=['CUCHARAS', 'TENEDORES', 'CUCHILLOS', 'PLATO'])
        self.df.loc[2,"detalle"] = "serie de utensilios"
        self.df.loc[2,"resultado"] = utensilios.to_string()
        print("punto_3")
        print("utensilios") 

    def punto_4(self):
        # Usar el dataset 'review' en lugar de 'self.df'
        total_filas = len(self.review) # Número de filas en el dataset Wine Reviews
        self.df.loc[3,"resultado"] = total_filas + 3 # Sumar 3 al total de filas de review
        self.df.loc[3,"detalle"] = "Longitud del dataset Wine Reviews más 3"
        ruta_archivo = r"C:\repositorios\wilmerarce_entregable2\archive (2)\winemag-data-130k-v2.csv"
        print("punto_4") 

    def punto_5(self):
        self.df.loc[4,"resultado"] = len(self.df)+4
        print("punto_5")

    def punto_6(self):
        self.df.loc[5,"resultado"] = "punto_5.csv"
        print("punto_6")

    def punto_7(self):
        self.df.loc[6,"resultado"] = len(self.df)+6
        print("punto_7") 

    def punto_8(self):
        self.df.loc[7,"resultado"] = len(self.df)+7
        print("punto_8")

    def punto_9(self):
        self.df.loc[8,"resultado"] = len(self.df)+8
        print("punto_9")

    def punto_10(self):
        self.df.loc[9,"resultado"] = len(self.df)+9
        print("punto_10") 

    def punto_11(self):
        self.df.loc[10,"resultado"] = len(self.df)+10
        print("punto_11") 

    def punto_12(self,num=100):
        self.df.loc[11,"resultado"] = len(self.df)+11
        print("punto_12") 
    
    def ejecutar(self):
        self.punto_1()     
        self.punto_2() 
        self.punto_3() 
        self.punto_4() 
        self.punto_5() 
        self.punto_6() 
        self.punto_7() 
        self.punto_8() 
        self.punto_9() 
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad3.csv", index=False) # Guarda sin el indice

if __name__ == "__main__":
    act = actividad3("C:\repositorios\wilmerarce_entregable2\archive (2)\winemag-data-130k-v2.csv")
    act.ejecutar()

