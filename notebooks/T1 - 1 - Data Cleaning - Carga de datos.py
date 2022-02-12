# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:59:26 2021

@author: u161677
"""
# =============================================================================
# Seleccion del Directorio de Trabajo (wd):
# =============================================================================
# 
# 1° Con pwd determinamos el directorio actual
pwd
# 'C:\\Users\\u161677\\Documents\\Python\\script'

# 2° Seleccionamos el WD: 
# Desde el simbolo de la carpeta (arriba derecha), seleccionamos el wd 

pwd
# 'C:\Users\u161677\Documents\GitHub\python-ml-course\notebooks'
#
# 3° Desde la libreria os: 
os.getcwd()
os.chdir(r'C:\Users\u161677\Documents\GitHub\python-ml-course')
os.getcwd()

# =============================================================================
# Importamos libreria
# =============================================================================

import pandas as pd
import os

# =============================================================================
# 21 a 23.- Función: pd.read
# =============================================================================

# Path absoluto: Donde se describe todo el path y archivo
data = pd.read_csv("C:\\Users\\u161677\\Documents\\GitHub\\python-ml-course\\datasets\\titanic\\titanic3.csv")
data.head()

data2 = pd.read_csv('C:/Users/u161677/Documents/GitHub/python-ml-course/datasets/titanic/titanic3.csv')
data2.head()


data3 = pd.read_csv(r'C:\Users\u161677\Documents\GitHub\python-ml-course\datasets\titanic\titanic3.csv')
data3.head()

data4 = pd.read_csv(r'C:/Users/u161677/Documents/GitHub/python-ml-course/datasets/titanic/titanic3.csv')
data4.head()


# Este formato No corre sin la r 
# data30 = pd.read_csv('C:\Users\u161677\Documents\GitHub\python-ml-course\datasets\titanic\titanic3.csv')



# Path relativo: Incluye el WD en el path
data5 = pd.read_csv("..\\python-ml-course\\datasets\\titanic\\titanic3.csv")
data5.head()

data6 = pd.read_csv('../python-ml-course/datasets/titanic/titanic3.csv')
data6.head()


data7 = pd.read_csv(r'..\python-ml-course\datasets\titanic\titanic3.csv')
data7.head()

data5 = pd.read_csv(r'../python-ml-course/datasets/titanic/titanic3.csv')
data5.head()

# Este formato NO corre sin la r
# data31 = pd.read_csv('..\python-ml-course\datasets\titanic\titanic3.csv')

# =============================================================================
# Osbservaciones:
# 1.- Arcchivos .csv y .txt pueden ser abiertos desde la funcion read.
# 2.- Antes de convertir un archivo en data frame, conviene abrirlo con un Notepad para ver su estructura.
#  ej: si las columnas estan separadas por ","o por ";" o bien por "|"
#  ej: ver si utiliza simboloes de escape como las comillas "Apellido, Nombre", etc 
# =============================================================================
# Parametros de la funcion pd.read.csv()
"""
Ejemplos de los parámetros de la función read_csv
read.csv(filepath="path_absoluto/titanic3.csv",
        sep = ",", 
        dtype={"ingresos":np.float64, "edad":np.int32}, 
        header=0,names={"ingresos", "edad"},
        skiprows=12, index_col=None, 
        skip_blank_lines=False, na_filter=False
        )
"""
# Parametros para el cabio de cabecera:
# header = None y names =  {elementos del conjunto separados por coma}

# =============================================================================
# 24.- Funcion OPEN
# =============================================================================
# La funcion OPEN se emplea cuando los datos a tratar son muy grandes (Gbytes).
# Por defecto, el fichero se abre en modo solo lectura (r), para poder entender cuangrande es.!!
# La Open ira leyendo linea a linea, permitiendo así fraccionar el fichero en diferentes maquinas.
# Ej: Vamos a trabajar con: 
# Archivo: Tab Customer Churn Model.txt
# Path: C:/Users/u161677/Documents/GitHub/python-ml-course/datasets/customer-churn-model

# Aperturamos OPEN solo lectura (r)
data3 = open('C:/Users/u161677/Documents/GitHub/python-ml-course/datasets/customer-churn-model/Tab Customer Churn Model.txt','r')
# data3 = open(r'../python-ml-course/datasets/customer-churn-model/Tab Customer Churn Model.txt','r')


# METODO: Arreglo que permite anteponer el df y luego las funciones.
#  df = data.funcion1().funcion2().funcion3()

cols = data3.readline().strip().split(",")
n_cols = len(cols)






































