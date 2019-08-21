
########################################
## Universidad del Valle de Guatemala ##
## Autores:                           ##
##      Andrea Cordon                 ##
##      Michelle Bloomfield           ##
########################################


import random 
import math 

class Integral2:
    ##Se ingresa mi integral
    def funcion(self, x, y):
        return (math.exp(-1*((1/x)-1) * (1+y))/ (x**2)) * ((1/x)-1)


    ##Monte carlo
    def monte_carlo(self, iteraciones):
        x = 0
        for i in range(1, iteraciones):
            x = x + self.funcion(random.random(), random.random())
        return x/iteraciones

def main():
    integral2 = Integral2()

    print("Resultado con 100 iteraciones: ", integral2.monte_carlo(100))
    print("Resultado con 10,000 iteraciones: ", integral2.monte_carlo(10000))
    print("Resultado con 1,000,000 iteraciones: ", integral2.monte_carlo(1000000))


if __name__== '__main__':
    main()