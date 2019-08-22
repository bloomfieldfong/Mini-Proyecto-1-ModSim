
########################################
## Universidad del Valle de Guatemala ##
## Autores:                           ##
##      Andrea Cordon                 ##
##      Michelle Bloomfield           ##
########################################

import random
import matplotlib.pyplot as plt
import datetime, time



class Generadores:
    ## Generador 1: x = 5^5* xn-1 mod(2^35 -1)
    def generador1(self, seed, iteraciones):
        x = []
        x.append(seed)
        for i in range(1,iteraciones):
            y = ((5**5*(x[i-1]))%(2**35-1)) 
            x.append(y)
        return x

    ## Generador 2: x = 7^5* xn-1 mod(2^31 -1)          
    def generador2(self, seed, iteraciones):
        x = []
        x.append(seed)
        for i in range(1,iteraciones):
            y = (7**5 * (x[i-1])) % (2**31 -1)
            x.append(y)

        return x

    ## Generador 3:  x = math.random()
    def generador3(self, iteraciones):
        x = []
        for i in range(1, iteraciones):
            x.append(random.random())
        return x

    ##Cuenta en el rango que se especifique
    def count(self, lista, inf, sup, generador): 
        cuantos = 0
        listaNueva = []

        if generador == 1:
            for x in lista:
                listaNueva.append((x/(2**35-1)))
        if generador == 2:
            for x in lista:
                listaNueva.append((x/(2**31-1)))
        if generador == 3:
            listaNueva = lista
        for x in listaNueva: 
            if x>= inf and x<= sup: 
                cuantos+= 1 
        return cuantos

    def graficar(self,lista, porcentaje):
        inf = 0.0
        sup = 0.1
        x = 0
        
        for i in lista:
            x = x + int(i)
            
        for i in range(0,10):
            print(str(inf)+"-"+str(sup)+" "+str(int(lista[i]*porcentaje)*"*")+" " +str(round(((lista[i]/(x))*100),2))+ "% - Total: " + str(lista[i]))
            inf = round((inf + 0.1), 2)
            sup = round((sup + 0.1),2)

def main():

    salida = True

    generador = Generadores()
    while salida == True:
        print("Generador 1: x = 5^5* xn-1 mod(2^35 -1)")
        print("Generador 2: x = 7^5* xn-1 mod(2^31 -1)")
        print("Generador 3:  x = math.random()")
        ingreso = input("Ingrese que generador quiere realizar (1,2 o 3): ")

        if(ingreso == "1"):

            ##Lista de numeros contados de 0 a 1
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
            ##superior e inferior
            inf = 0
            sup = 0.1
            
            ##Lista de iteracionn con un seed de time.time
            itera_1= generador.generador1(time.time(), 100)
            itera_2 = generador.generador1(time.time(), 5000)
            itera_3 = generador.generador1(time.time(), 100000)

            ##Se itera para cada lista y cuenta por cada .1
            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup,1))
                lista_2.append(generador.count(itera_2, inf, sup,1))
                lista_3.append(generador.count(itera_3, inf,sup,1))
                inf = inf + 0.1
                sup = sup + 0.1
          
            ##Graficar cada lsita
            print("\nGenerador 1: 100 Corridas\n")
            generador.graficar(lista_1, 4)
            print("\nGenerador 1: 5000 Corridas\n")
            generador.graficar(lista_2,0.1)
            print("\nGenerador 1: 100000 Corridas\n")
            generador.graficar(lista_3,0.005)
           
            

        if(ingreso == "2"):

            ##Lista de numeros contados de 0 a 1
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
            ##superior e inferior
            inf = 0
            sup = 0.1
            
            ##Lista de iteracionn con un seed de time.time
            itera_1= generador.generador2(time.time(), 100)
            itera_2 = generador.generador2(time.time(), 5000)
            itera_3 = generador.generador2(time.time(), 100000)


            ##Se itera para cada lista y cuenta por cada .1
            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup,2))
                lista_2.append(generador.count(itera_2, inf, sup,2))
                lista_3.append(generador.count(itera_3, inf,sup,2))
                inf = inf + 0.1
                sup = sup + 0.1

            ##Graficar cada lsita
            print("\nGenerador 2: 100 Corridas\n")
            generador.graficar(lista_1, 4)
            print("\nGenerador 2: 5000 Corridas\n")
            generador.graficar(lista_2, 0.1)
            print("\nGenerador 2: 100000 Corridas\n")
            generador.graficar(lista_3, 0.005)
           
            


        if(ingreso == "3"):

            ##Lista de numeros contados de 0 a 1
            lista_1 = []
            lista_2 = []
            lista_3 = []
            
             ##superior e inferior
            inf = 0
            sup = 0.1
            
            ##Lista de iteracionn con un seed de time.time
            itera_1= generador.generador3( 100)
            itera_2 = generador.generador3(5000)
            itera_3 = generador.generador3(100000)

            ##Se itera para cada lista y cuenta por cada .1
            for x in range(0, 10):
                lista_1.append(generador.count(itera_1, inf, sup,3))
                lista_2.append(generador.count(itera_2, inf, sup,3))
                lista_3.append(generador.count(itera_3, inf,sup,3))
                inf = inf + 0.1
                sup = sup + 0.1
         
            ##Graficar
            print("\nGenerador 3: 100 Corridas\n")
            generador.graficar(lista_1, 4)
            print("\nGenerador 3: 5000 Corridas\n")
            generador.graficar(lista_2, 0.1)
            print("\nGenerador 3: 100000 Corridas\n")
            generador.graficar(lista_3, 0.005)

        if(ingreso > "3"):
            salida = False           
            



if __name__ == "__main__":
    main()
