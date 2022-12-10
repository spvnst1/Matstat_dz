import random
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import poisson

'''theta=6
def get_array(v):
    array=[]
    for i in range(v):
        n = random.uniform(0, 1)
        l = 0
        j = 0
        while n > l:
            l += (theta**j/factorial(j)*e**(-theta)/(1-e**(-theta)))
            j += 1
            array.append(j)
    return array '''
a=[8, 3, 4, 5, 6, 5, 3, 7, 6, 1, 7, 4, 5, 4, 4, 7, 5, 8, 6, 7, 4, 4, 9, 10, 5, 4, 1, 5, 7, 4, 5, 4, 12, 8, 6, 5, 6, 4, 5, 9, 3, 4, 5, 11, 9, 5, 3, 2, 2, 6, 2, 7, 5, 1, 5, 6, 6, 7, 9, 4, 6, 6, 5, 4, 6, 11, 2, 4, 9, 4, 3, 2, 2, 4, 4, 3, 6, 8, 4, 4, 5, 4, 7, 5, 3, 7, 4, 12, 8, 3, 4, 5, 5, 3, 8, 7, 5, 10, 3, 7, 6, 6, 6, 8, 5, 4, 6, 2, 5, 2, 6, 7, 5, 4, 5, 7, 11, 7, 15, 10, 6, 5, 8, 6, 5, 5, 4, 6, 4, 3, 6, 8, 3, 8, 4, 2, 6, 9, 3, 5, 8, 5, 6, 7, 9, 5, 3, 9, 7, 8, 4, 5, 3, 6, 5, 4, 8, 4, 7, 12, 7, 7, 8, 5, 4, 3, 3, 9, 10, 4, 10, 7, 9, 8, 5, 4, 5, 6, 5, 5, 2, 2, 5, 7, 3, 3, 8, 8, 3, 7, 4, 6, 6, 7, 10, 4, 6, 7, 6, 6, 4, 7, 8, 6, 4, 5, 8, 6, 8, 3, 5, 6, 3, 7, 2, 10, 6, 5, 6, 6, 5, 4, 7, 7, 6, 8, 4, 4, 5, 7, 5, 6, 6, 8, 3, 3, 6, 2, 8, 6, 5, 7, 8, 3, 2, 5, 6, 7, 9, 5, 5, 3, 3, 5, 3, 6, 7, 4, 6, 7, 6, 6, 7, 8, 5, 2, 8, 5, 3, 7, 5, 8, 5, 3, 5, 4, 7, 6, 10, 4, 13, 3, 4, 3, 5, 4, 10, 8, 4, 2, 6, 8, 9, 6, 6, 3, 7, 5, 5, 3, 5, 8, 7, 8, 7, 7, 6, 4, 6, 7, 9, 4, 5, 3, 3, 8, 6, 4, 10, 8, 8, 7, 6, 3, 6, 8, 4, 10, 6, 3, 4, 10, 4, 4, 7, 8, 4, 5, 7, 4, 7, 8, 4, 3, 5, 5, 8, 2, 4, 6, 4, 6, 3, 8, 7, 6, 3, 8, 7, 4, 8, 5, 11, 6, 8, 9, 2, 4, 8, 9, 12, 5, 5, 6, 3, 7, 6, 10, 6, 6, 10, 4, 3, 8, 7, 6, 6, 7, 6, 6, 6, 6, 9, 2, 8, 8, 3, 9, 3, 4, 7, 5, 3, 5, 6, 8, 3, 3, 3, 9, 5, 7, 6, 11, 8, 4, 3, 7, 5, 6, 8, 4, 3, 4, 6, 7, 7, 4, 4, 5, 12, 7, 4, 3, 4, 5, 6, 7, 3, 9, 6, 5, 9, 3, 4, 4, 4, 11, 6, 9, 6, 5, 3, 4, 7, 6, 4, 9, 2, 4, 5, 3, 10, 4, 8, 6, 11, 2, 4, 6, 6, 9, 4, 3, 5, 10, 7, 6, 4, 7, 7, 6, 8, 8, 5, 3, 5, 8, 8, 6, 5, 4, 6, 9, 4, 11, 6, 7, 6, 9, 5, 8, 12, 5, 3, 6, 10, 3, 4, 5, 2, 3, 7, 5, 4, 12, 11, 9, 6, 7, 5, 10, 6, 10, 5, 2, 9, 9, 5, 9, 4, 2, 7, 5, 5, 6, 4, 5, 6, 4, 9, 4, 5, 8, 7, 7, 7, 6, 7, 5, 8, 10, 5, 2, 6, 2, 3, 4, 3, 6, 5, 5, 8, 4, 7, 8, 5, 4, 6, 3, 7, 9, 5, 6, 7, 7, 6, 10, 4, 5, 5, 7, 7, 7, 7, 9, 9, 2, 4, 9, 6, 9, 13, 5, 8, 6, 7, 2, 3, 10, 7, 6, 9, 4, 6, 2, 7, 11, 6, 8, 6, 5, 7, 6, 4, 11, 7, 6, 11, 7, 8, 5, 4, 3, 8, 6, 4, 2, 4, 3, 7, 10, 6, 6, 6, 8, 1, 8, 7, 3, 9, 3, 9, 8, 7, 4, 9, 6, 6, 2, 5, 5, 4, 6, 1, 5, 12, 13, 11, 3, 6, 9, 7, 4, 6, 2, 8, 4, 8, 12, 8, 8, 8, 6, 7, 6, 8, 4, 1, 5, 7, 7, 4, 6, 7, 8, 8, 4, 6, 14, 5, 7, 5, 2, 9, 4, 4, 9, 9, 5, 5, 4, 10, 4, 4, 4, 5, 7, 4, 6, 6, 5, 6, 6, 3, 3, 8, 9, 5, 3, 5, 12, 7, 7, 5, 6, 7, 10, 9, 5, 3, 1, 8, 4, 6, 4, 10, 3, 5, 12, 3, 4, 6, 3, 6, 7, 6, 3, 9, 6, 7, 4, 4, 5, 9, 9, 7, 6, 5, 9, 9, 6, 5, 3, 6, 4, 8, 9, 7, 8, 8, 7, 6, 6, 7, 2, 7, 4, 4, 7, 6, 3, 10, 4, 10, 1, 4, 8, 11, 5, 7, 5, 5, 6, 6, 6, 7, 7, 7, 4]

razmer=(len(a))
k=1+math.ceil(math.log2(razmer))
data_binom = poisson.rvs(mu=6, size=10000)




#plt.hist(a, bins=k,color='blue')
plt.hist(a,bins=k,density=True, label='выборка')
plt.title('Гистограмма для выборки объемом 800')
ax = sns.kdeplot(data_binom,color='black')

plt.show()