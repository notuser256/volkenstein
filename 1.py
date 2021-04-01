def f(q1,q2,e_0,e,r):
    return q1*q2/(4*3.14*e_0*e*pow(r,2))
r=0.5*pow(10,-10)
q1=q2=1.6*pow(10,-19)
e_0=8.85*pow(10,-12)
e=1
k=f(q1,q2,e_0,e,r)*pow(10,8)
print(f(q1,q2,e_0,e,r))
print('{:.11f}'.format(f(q1,q2,e_0,e,r)))


