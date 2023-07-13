""" def add(a,b):
    c=a+b
    d=a*b
    e=a-b
    return c,d,e

x=add(10,20)
print(x)     #(30, 200, -10)


def add(a,b):
    c=a+b
    d=a*b
    e=a-b
    return c,d,e
x,y,z=add(10,20)
print(x)   #30
print(y)   #200
print(z)   #-10


def add(a,b):
    c=a+b
    d=a*b
    e=a-b
    return c,d,e
x,y=add(10,20)
print(x)
print(y)
#to many value to unpacking """