import numpy as np
import matplotlib.pyplot as plt
import random

class Helecho:

    def f1(self, x, y):
        return [x*0.86 + y*0.04+ 0.0, x*-0.04 + y* 0.85 + 1.6]

    def f2(self, x, y):
        return [-0.15*x + 0.28*y + 0.0, x*0.26+ y*0.24+ 0.44]

    def f3(self, x, y):
        return [x*0.2 + y*-0.26 + 0.0, x*0.23 + y*0.22 + 1.6]

    def f4(self, x, y):
        return [x*0.0 + y*0.0, x*0.0 + y*0.16]

    def eleccion(self, funciones, probabilidades):
        resultado = []
        for dato, prob in zip(funciones,probabilidades):
            resultado += [dato] * int(prob * 100)
        return random.choice(resultado)

    def resultado_funciones(self, x, y):
        return [self.f1(x,y), self.f2(x,y), self.f3(x,y), self.f4(x,y)]

    def helecho(self, probabilidades, n = 100000):
        pos_x = []
        pos_y = []

        pos_x.append(0)
        pos_y.append(0)

        for i in range(1,n):
            funcion = self.resultado_funciones(pos_x[i-1], pos_y[i-1])
            resultado= self.eleccion(funcion, probabilidades)
            pos_x.append(resultado[0])
            pos_y.append(resultado[1])
        return pos_x, pos_y
    
            

def main():
    helecho = Helecho()
    probabilidades = [0.85, 0.07, 0.07, 0.01]
    choices = helecho.helecho(probabilidades)
    plt.plot(choices[0], choices[1], ".")
    plt.show()

if __name__ == "__main__":
    main()
