'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
import random


'''
idea is eqn given
_______________
|(--r--.--r--)|
_______________
square area = 2r * 2r => 4r^2
circle area = pi r^2 

pi = total_inside_cirle/total

'''
N = 100000
inside_circle = 0
for  i in range(N):
    x = random.random()
    y = random.random()

    if (x**2 + y **2)**.5 < 1:
        inside_circle +=1

print((inside_circle/N)*4)
