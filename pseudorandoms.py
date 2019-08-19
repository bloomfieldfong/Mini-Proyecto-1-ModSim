import random

x =[]

x.append(0)

def generador1(x_anterior):
    print((5^5 * (x_anterior)) % (2^35 -1))
    return (5^5 * (x_anterior)) % (2^35 -1)

def generador2(x_anterior):
    return (7^5 * (x_anterior)) % (2^31 -1)



for i in range(1,1000):
    y = generador2(x[i-1])
    x.append(y)
print(x)
