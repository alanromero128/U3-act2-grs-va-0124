import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de países con 4 elementos por lista
esp = ['España', 'Madrid', True, 47.4]
mex = ['México', 'CDMX', False, 126.7]
fra = ['Francia', 'París', True, 67.7]
arg = ['Argentina', 'Buenos Aires', False, 45.8]
jap = ['Japón', 'Tokio', False, 125.7]

# Creamos una lista de listas 
lista_paises = [esp, mex, fra, arg, jap]

# utilizar pandas para organizar la tabla (DataFrame o marco de datos)
df_paises = pd.DataFrame(lista_paises, columns=["País", "Capital", "Pertenece_UE", "Poblacion_Millones"])
print(df_paises)
df_paises.to_csv("paises.csv", index=False)

# Crear gráfica de líneas 
# Donde X es País en el eje horizontal 
# donde Y es Población (millones) en el eje vertical   
plt.plot(df_paises["País"], df_paises["Poblacion_Millones"])
plt.title("Gráfica de países 0124")
plt.xlabel("Nombre del país")
plt.ylabel("Población (millones)")
plt.show()

# creamos gráfica de puntos
plt.scatter(df_paises["País"], df_paises["Poblacion_Millones"])
plt.show()

# Gráfica de barras
plt.bar(df_paises["País"], df_paises["Poblacion_Millones"])
# Etiquetas y título
plt.title("Países 0124")
plt.xlabel("Los países")
plt.ylabel("Población (millones)")
# mostrar gráfica
plt.show()

# ordenar la gráfica de barras de manera descendente
# de la más grande a la más pequeña
df_paises_ordenar = df_paises.sort_values("Poblacion_Millones", ascending=False)
plt.bar(df_paises_ordenar["País"], df_paises_ordenar["Poblacion_Millones"])
plt.show()

# coloreando barra
df_paises_ordenar = df_paises.sort_values("Poblacion_Millones", ascending=False)
plt.bar(df_paises_ordenar["País"], df_paises_ordenar["Poblacion_Millones"],      
        color=["b", "g", "c", "m", "y"]) 
plt.show()

# Gráfica de pastel 
plt.pie(df_paises["Poblacion_Millones"], labels=df_paises["País"])
plt.show()
print("Programa hecho por Alan Romero 0124")