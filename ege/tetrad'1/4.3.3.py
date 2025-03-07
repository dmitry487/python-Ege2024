import numpy as np
from numpy import trapezoid
import matplotlib.pyplot as plt
import math as m

x=np.arange(0,11,1)
def f(x): return abs(m.cos(x*m.e**(m.cos(x)+m.log(x+1,m.e))))
y=[x for x in range(0,11)]
for i in range(len(y)):
    y[i]=f(y[i])
plt.plot(x,y,c='r')
plt.fill_between(x,y)
plt.show()
area=trapezoid(y)
print(area)