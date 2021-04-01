import pylab
def F(q1,q2,e_0,e,r):
    return q1*q2/(4*3.14*e_0*e*pow(r,2))
e=1
r=[j/100 for j in range(2,11,2)]
delta=2*pow(10,-2)
q1=20*pow(10,-9)
q2=30*pow(10,-9)
e_0=8.85*pow(10,-12)
print(r)
f=[ F(q1,q2,e_0,e,j*pow(10,-2)) for j in range(2,11,2)]
print(len(f)==len(r))
pylab.xlabel("r,м")
pylab.ylabel("F,Н")
pylab.plot (r,f,color='blue')
pylab.show()
