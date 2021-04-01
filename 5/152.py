from math import sqrt
import pylab
def f(r,t,u,k,i,q):
    return sqrt(r*t/(9*3.14*u))*(k*i/(3.14*pow(q,2)))
u=32*pow(10,-3)
delta=100
T=[j for j in range(100,601,delta)]
q=0.3*pow(10,-9)
k=1.38*pow(10,-23)
r=8.31
ot=[f(r,ValuesT,u,k,5,q) for ValuesT in T]
pylab.plot(T,ot)
print(ot[1])
pylab.show()
