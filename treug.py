import random
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import triang

def imper_func(realisation,x):
    k=0
    for elem in realisation:
        if elem<=x:
            k +=1

    return k/len(realisation)

def Triangle(p):
    u = random.uniform(0, 1)
    if 0 < u < p:
        return round(sqrt(u*p),4)
    elif p < u < 1:
        return round(1-sqrt((1-u)*(1-p)),4)


theta = 0.4
array = []
for i in range(5):
    n = Triangle(theta)
    array.append(n)
print(array)
#sns.kdeplot(array)
#plt.grid

'''
z=[]
samples0=np.linspace(start=0,stop=1,num=1000)
for elem in samples0:
    z.append(imper_func(array,elem))

y_true=[triang.cdf(t,0.4) for t in samples0]
plt.plot(samples0,z,color='red')
plt.plot(samples0,y_true,color='black')
plt.title('Эмпирическая функция распределения при размере выборки 5')
#plt.stairs(z,color="red")

plt.xlim([0,1]) '''
#plt.show()
#print(array)
'''
numargs=triang.numargs
a=0.4
rv=triang(a)

dist=triang.rvs(0.4,size=1000)
distripution=np.linspace(0,np.minimum(rv.dist.b,3))
plt.plot(distripution,rv.pdf(distripution),color="black")

plt.show()
'''
'''sns.kdeplot(array)
plt.grid()
plt.show() '''
