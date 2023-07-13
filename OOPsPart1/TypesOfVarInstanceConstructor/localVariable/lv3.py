class test:
    x=20
    y=50
    def __init__(self,x):
        self.x=x
    def info(self):
        print(x)
        print(self.x)
        print(test.x)
        print(self.y)
        print(test.y)

t=test(30)
x=100
test.y=2000
t.info()
x=200
t.x=500
test.y=2500
t.y=3000
t.info()