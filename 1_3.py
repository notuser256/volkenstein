v1=10
v2=16
def v_middle(v1,v2):
    return 2*v1*v2/(v1+v2)
def u (v1,v2):
    return (v2-v1)/2
print(f"Ответ: Средняя скорость= {v_middle(v1,v2)}, Скорость реки= {u(v1,v2)}")