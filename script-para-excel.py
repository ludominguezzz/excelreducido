import numpy as np
import os

ruta = "C:/Users/Vaio/Documents/Doctorado/ANALISIS DE IMAGENES/405-CH1/28-11-23"
fechas = [ruta + "/" + file for file in os.listdir(ruta)]
for file in fechas:
    BD = np.genfromtxt(file, delimiter=' ', skip_header=0)
    BD2 = BD[:60, :60]
    np.savetxt(file, BD2, delimiter=" ", fmt='%.2f')


#datos = np.genfromtxt('j6-z1-cel1_a1[%].asc', delimiter=' ', skip_header=0)
#datos2 = datos[:60, :60]
#np.savetxt('prueba.csv', datos2, delimiter=" ", fmt='%.2f')

#### ver tecnica slicing para reacomodar el tamaño:  https://www.youtube.com/watch?v=HpLYgKU57eE

#datos2 = datos.reshape(50, 50)
#print(datos)

#np.savetxt('prueba.csv', datos, delimiter=" ", fmt='%.2f')
#print(datos)
#from funpymodeling.data_prep import todf
#datos_df = todf(datos)
#print(datos_df.shape)

