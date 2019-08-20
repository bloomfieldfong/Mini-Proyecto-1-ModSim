
########################################
## Universidad del Valle de Guatemala ##
## Autores:                           ##
##      Andrea Cordon                 ##
##      Michelle Bloomfield           ##
########################################

import random
import matplotlib.pyplot as plt
import time



class Generadores:
    ## Generador 1: x = 5^5* xn-1 mod(2^35 -1)
    def generador1(self, seed, iteraciones):
        x = []
        x.append(seed)
        for i in range(1,iteraciones):
            y = ((5**5*(x[i-1]))%(2**35-1)) %1
            x.append(y)
        return x

    ## Generador 2: x = 7^5* xn-1 mod(2^31 -1)          
    def generador2(self, seed, iteraciones):
        x = []
        x.append(seed)
        for i in range(1,iteraciones):
            y = (7**5 * (x[i-1])) % (2**31 -1)% 1
            x.append(y%1)
        return x

    ## Generador 3:  x = math.random()
    def generador3(self, iteraciones):
        x = []
        for i in range(1, iteraciones):
            x.append(random.random())
        return x

    ##Cuenta en el rango que se especifique
    def count(self, lista, inf, sup): 
        cuantos = 0 
        for x in lista: 
            if x>= inf and x<= sup: 
                cuantos+= 1 
        return cuantos

def main():

    generador = Generadores()
    while(True):
        print("Generador 1: x = 5^5* xn-1 mod(2^35 -1)")
        print("Generador 2: x = 7^5* xn-1 mod(2^31 -1)")
        print("Generador 3:  x = math.random()")
        ingreso = input("Ingrese que generador quiere realizar (1,2 o 3): ")

        if(ingreso == "1"):
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
            inf = 0
            sup = 0.1
            
            itera_1= generador.generador1(0.05, 100)
            itera_2 = generador.generador1(0.05, 5000)
            itera_3 = generador.generador1(0.05, 100000)

            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup))
                lista_2.append(generador.count(itera_2, inf, sup))
                lista_3.append(generador.count(itera_3, inf,sup))
                inf = inf + 0.1
                sup = sup + 0.1
            print(lista_2)
            

        if(ingreso == "2"):
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
            inf = 0
            sup = 0.1
            
            itera_1= generador.generador2(0.05, 100)
            itera_2 = generador.generador2(0.05, 5000)
            itera_3 = generador.generador2(0.05, 100000)

            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup))
                lista_2.append(generador.count(itera_2, inf, sup))
                lista_3.append(generador.count(itera_3, inf,sup))
                inf = inf + 0.1
                sup = sup + 0.1

        if(ingreso == "3"):
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
            inf = 0
            sup = 0.1
            
            itera_1= generador.generador3( 100)
            itera_2 = generador.generador3(5000)
            itera_3 = generador.generador3(100000)

            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup))
                lista_2.append(generador.count(itera_2, inf, sup))
                lista_3.append(generador.count(itera_3, inf,sup))
                inf = inf + 0.1
                sup = sup + 0.1



if __name__ == "__main__":
    main()
