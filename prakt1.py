import numpy as np
import matplotlib.pyplot as plt
import random

def sort_vybor(massiv):
    for i in range(0,len(massiv)):
        l=i
        for j in range(i+1,len(massiv)):
            if massiv[j] < massiv[l]:
                l=j
    t=massiv[i]
    massiv[i]=massiv[l]
    massiv[l]=t
    return massiv

X = np.random.randint(-20,20,30)
Y = np.random.randint(-20,20,30)
fig=plt.figure()
plt.plot(X,Y,'green')
print(X)
print(Y)

F=sort_vybor(X)
H=sort_vybor(Y)

plt.plot(X,Y,'green',F,H,'red')

plt.show()

print(F)
print(H)
