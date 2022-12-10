import random
from math import e,factorial,sqrt,fabs
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import poisson

def imper_func(realisation,x):
    k=0
    for elem in realisation:
        if elem<=x:
            k +=1

    return k/len(realisation)

theta = 6
array = []
samples0=np.arange(1,1000)
z=[]
n=[5,10,100,200,400,600,800,1000]
def get_array(v):
    array=[]
    for i in range(v):
        n = random.uniform(0, 1)
        l = 0
        j = 1
        while n > l:
            l += (theta**j/factorial(j)*e**(-theta)/(1-e**(-theta)))
            j += 1
        array.append(j-1)
    return array

def poisson_real(x,theta=6):
    rez=0
    for i in range(1,x+1):
        rez+=theta**i/factorial(i)
    return rez*(e**(-theta))/(1-e**(-theta))
X=np.arange(1,40)
Y=[poisson_real(x) for x in X]

array1=get_array(10000)
sns.kdeplot(array1)
plt.grid()

for elem in samples0:
    z.append(imper_func(array1,elem))
plt.stairs(z,np.append(samples0,1000),color='red')
plt.xlim([0,30])

r_values=list(range(100000))
dist=[poisson.cdf(r,6) for r in r_values]
plt.stairs(dist,color="black")
plt.stairs(Y,np.append(X,40),color='black')
plt.title('Эмпирическая функция распределения при размере выборки 1000') 
plt.show()
