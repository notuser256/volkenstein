import pylab
def f(p,u,r,t):
    return p*u/(r*t)
t_const=390
p_const=400*pow(10,3)
delta_p=50
p=[ j *pow(10,3) for j in range(0,401,delta_p)]
delta_t=20
t=[j for j in range(200,301,delta_t)]
u=32*pow(10,-3)
r=8.31
q_p=[f(pValues,u,r,t_const) for pValues in p]
q_t=[f(p_const,u,r,tValues) for tValues in t]
pylab.plot(p,q_p)
pylab.xlabel("P,ПА")
pylab.ylabel("q,кг/м^3")
pylab.figure(2)
pylab.plot(t,q_t)
pylab.xlabel("T,K")
pylab.ylabel("q,кг/м^3")
pylab.show()

