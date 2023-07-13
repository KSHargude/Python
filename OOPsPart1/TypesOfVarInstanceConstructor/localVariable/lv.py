x=10
class test:
    x=20
    def __init__(self,x):
        self.x=x
    def info(self):
        print(x)
        print(self.x)
        print(test.x)
t=test(30)
t.info()