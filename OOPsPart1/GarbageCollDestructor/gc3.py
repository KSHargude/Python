import time
class test:
    def __init__(self):
        print("constructor")
    def __del__(self):       #self is mandetory
        print("destructor")

t=test()
t1=test()
t2=t
t3=t1
t4=t2
print("csd")
del t
time.sleep(2)
print("csd1")
del t1
del t2
time.sleep(2)
print("csd2")
del t3
del t4
time.sleep(2)
print("csd3")
