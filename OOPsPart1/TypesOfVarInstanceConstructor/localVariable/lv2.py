class test:
    x=20
    def __init__(self,x):
        self.x=x
    def info(self):
        print(x)
        print(self.x)
        print(test.x)

t=test(30)
x=100
t.info()
x=200
t.x=500
t.info()

#if instance not present then static and if local not present then global i=s l=g