import math

x=int(input("masukan nilai x="))
coba =1
a = 0
b=1
while coba>0.001:
    f_x = 0
    f_y = 0
    for i in range(a):
        f_x += (3**i)*x**i/math.factorial(i)

    for j in range(b):
        f_y += (3**j)*x**j/math.factorial(j)
    print("suku ke",a,"=",f_x)
    print("suku ke",b,"=",f_y)

    coba = f_y-f_x
    a+=1
    b+=1
    print("hasil selisih =",coba)
