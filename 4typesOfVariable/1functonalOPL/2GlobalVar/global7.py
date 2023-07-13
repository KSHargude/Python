x=20
def f1():
    x=100
    print(x)
    print(globals()['x'])
f1()