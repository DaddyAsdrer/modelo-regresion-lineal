import os
import pickle as pkl
import matplotlib.pyplot as plt
import pandas as pd

class Modelo():
    def __init__(self):
        self.m = 0
        self.b = 0
    
    def entrenamiento(self):
        while True:
            try:
                datos = input('Introduce los nombres de los ficheros (datos1.csv - datos2.csv): ').split(' - ')
                df1 = pd.read_csv(datos[0])
                df2 = pd.read_csv(datos[1])
                break
            except FileNotFoundError: print('Error al detectar archivos, intentalo otra vez...\n')
    
        self.columna_x = df1.iloc[:,1]
        x_pro = sum(self.columna_x) / len(self.columna_x)
        self.columna_y = df2.iloc[:,1]
        y_pro = sum(self.columna_y) / len(self.columna_y)
        
        m_numerador = sum((self.columna_x[i] - x_pro) * (self.columna_y[i] - y_pro) for i in range(len(self.columna_x)))
        m_denominador = sum((self.columna_x[i] - x_pro) ** 2 for i in range(len(self.columna_x)))
        
        self.m = m_numerador / m_denominador
        self.b = y_pro - self.m * x_pro
        
    def predecir(self, inde):
        return self.m * inde + self.b
    
    def graficar(self):
        plt.scatter(self.columna_x,self.columna_y)
        plt.show()

directorio = os.path.dirname(os.path.abspath(__file__))
direccion_modelo = os.path.join(directorio,'regre_modelo.pkl')
modelo = pkl.load(open(direccion_modelo,'rb'))

print(f'Los datos del modelo son m = {modelo.m} y b = {modelo.b}')
