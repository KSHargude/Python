import time
class test:
    def __init__(self):
        print("constructor")
    def __del__(self):       #self is mandetory
        print("destructor")

t=test()
t1=t
print("csd")
del t
time.sleep(2)
print("csd")
del t1
time.sleep(2)
print("csd2")