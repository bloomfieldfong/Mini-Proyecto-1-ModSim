
########################################
## Universidad del Valle de Guatemala ##
## Autores:                           ##
##      Andrea Cordon                 ##
##      Michelle Bloomfield           ##
########################################


import random 
import math 

class Integral1:
    ##Se ingresa mi integral
    def funcion(self, x):
        return 2*(math.exp(-((1/x) -1)**2)/ x**2)


    ##Monte carlo
    def monte_carlo(self, iteraciones):
        x = 0
        for i in range(1, iteraciones):
            x = x + self.funcion(random.random())
        return x/iteraciones

def main():
    integral1 = Integral1()

    print("Resultado con 100 iteraciones: ", integral1.monte_carlo(100))
    print("Resultado con 10,000 iteraciones: ", integral1.monte_carlo(10000))
    print("Resultado con 1,000,000 iteraciones: ", integral1.monte_carlo(1000000))


if __name__== '__main__':
    main()