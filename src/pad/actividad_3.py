import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class actividad3:
    def __init__(self):
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
        self.df.loc[3,"resultado"] = len(self.df)+3
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
        self.df.to_csv("actividad3.csv")

act = actividad3()
act.ejecutar()