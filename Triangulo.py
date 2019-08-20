import numpy as np
import matplotlib.pyplot as plt
import random

class Triangulo:

    def f1(self, x, y):
        return [x/2, y/2]

    def f2(self, x, y):
        return [x/2 + 0.25, y/2 ]

    def f3(self, x, y):
        return [x/2 + 0.25, y/2 + 0.5]
    def eleccion(self, funciones, probabilidades):
        resultado = []
        for dato, prob in zip(funciones,probabilidades):
            resultado += [dato] * int(prob * 100)
        return random.choice(resultado)

    def resultado_funciones(self, x, y):
        return [self.f1(x,y), self.f2(x,y), self.f3(x,y)]

    def triangulo(self, probabilidades, n = 100000):
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
    triangulo = Triangulo()
    probabilidades = [0.33, 0.33, 0.33]
    choices = triangulo.triangulo(probabilidades)
    plt.plot(choices[0], choices[1], ".")
    plt.show()

if __name__ == "__main__":
    main()
