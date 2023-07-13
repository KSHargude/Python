x=20
def f1():
    global x
    x=50
    print(x)
x=100
x=200
def f2():
    x=40
    x=30
    print(x)
x=300
f1()
x=400
f2()