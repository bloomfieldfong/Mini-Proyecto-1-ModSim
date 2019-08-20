import numpy as np
import matplotlib.pyplot as plt
import random

##Cantidad de iteraciones que se realizaran
n = 100000

##Se guardan todas las posibles soluciones en donde se escogera cual 
resultado= []

##x y y inicial
x = 0
y = 0

##Se guardas las x y las y que se escogeran
choicesx = []
choicesy = []

for i in range(0,n):

    ##se define las funciones 
    f1 = [x*0.86 + y*0.04+ 0.0, x*-0.04 + y* 0.85 + 1.6]

    f2 = [-0.15*x + 0.28*y + 0.0, x*0.26+ y*0.24+ 0.44]

    f3 =  [x*0.2 + y*-0.26 + 0.0, x*0.23 + y*0.22 + 1.6]

    f4 = [x*0.0 + y*0.0, x*0.0 + y*0.16]
            
    ##Conjunto de funciones posibles funciones
    F = [f1, f2, f3, f4]

    ##Probabilidades de que pasen cada funcion
    ## f1 = 0.85
    ## f2 = 0.07
    ## f3 = 0.07
    ## f4 = 0.01
    p = 

    ##dato = f1, f2, f3, f4
    ##p = probabilidad
    ##agrupa nuestras funciones y crea 100 datos con su probabilidad y escoge una de los 100

    for dato, prob in zip(F, p):
        resultado += [dato] * int(prob * 100)

    ##Agarra un dato random de mi lista
    hola = random.choice(resultado)
    ##Se agrega la variable x a 
    x = hola[0]
    choicesx.append(x)
    y = hola[1]
    choicesy.append(y)
    resultado = []


##Plootea los puntos en x y y 
plt.plot(choicesx, choicesy, ".")

plt.show()
