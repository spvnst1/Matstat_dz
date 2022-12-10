import random
from math import e,factorial
import matplotlib.pyplot as plt
import seaborn as sns

theta = 6
n = 10

array = []

for i in range(200):
    n = random.uniform(0, 1)
    l = 0
    j = 0
    while n > l:
        l += (theta**j/factorial(j)*e**(-theta)/(1-e**(-theta)))
        j += 1
    array.append(j)
print(array)