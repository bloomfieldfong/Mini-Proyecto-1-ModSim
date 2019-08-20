import random

primero = 0.05
x =[]

x.append(primero)

def generador1(x_anterior):
    xn = (5**5*x_anterior)%(2**35-1)
    return xn

def generador2(x_anterior):
    xn = ((7**5 * (x_anterior)) % (2**31 -1))
    return xn


def count(x):
    x1, x2, x3, x4, x5, x6, x7, x8, x9 ,x10 = 0
    for i in x:
        if(x[i]<= 0.1):
            
    return x

    
########################################### GENERADOR 1  ###########################################
while(True):

    print("Generador 1: x = 5^5* xn-1 mod(2^35 -1)")
    print("Generador 2: x = 7^5* xn-1 mod(2^31 -1)")
    print("Generador 3:  x = math.random()")
    print("1. Generador 1 - 100 vueltas")
    print("2. Generador 1 - 5000 vueltas")
    print("3. Generador 1 - 10000 vueltas")
    print("4. Generador 2 - 100 vueltas")
    print("5. Generador 2 - 5000 vueltas")
    print("6. Generador 2 - 10000 vueltas")
    print("7. Generador 3 - 100 vueltas")
    print("8. Generador 3 - 5000 vueltas")
    print("9. Generador 3 - 10000 vueltas")
    print("")
    ingreso = input("Ingrese el numero que desea realizar")


    if(ingreso == '1'):
        ##Generador 1: para 100 corridas

        for i in range(1,100):
            y = generador1(x[i-1])%1
            x.append(y)
        print(x)

    if(ingreso == 2):
        ##Generador 1: para 5000 corridas

        for i in range(1,5000):
            y = generador1(x[i-1])%1
            x.append(y)

    if(ingreso == 3):
        ##Generador 1: para 100000 corridas

        for i in range(1,100000):
            y = generador1(x[i-1])%1
            x.append(y)

########################################### GENERADOR 2  ###########################################
        ##Generador 2: para 100 corridas
    if(ingreso == '4'):
        for i in range(1,100):
            y = generador2(x[i-1])%1
            x.append(y)
        print(x)

    if(ingreso == 5):
        ##Generador 2: para 5000 corridas

        for i in range(1,5000):
            y = generador2(x[i-1])%1
            x.append(y)

    if(ingreso == 6):
        ##Generador 2: para 100000 corridas

        for i in range(1,100000):
            y = generador2(x[i-1])%1
            x.append(y)


########################################### GENERADOR 3  ###########################################
    if(ingreso == 7):
        for i in range(1,100):
            x.append(random.randrange(1))
            print(x)

    if(ingreso == 8):
        for i in range(1,500):
            x.append(random.randrange(1))
            print(x)


    if(ingreso == 9):
        for i in range(1,100000):
            x.append(random.randrange(1))
            print(x)
