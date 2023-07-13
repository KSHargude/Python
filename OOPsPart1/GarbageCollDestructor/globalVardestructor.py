import time
class test:
    def __init__(self):
        print("constructor")
    def __del__(self):       #self is mandetory
        print("destructor")

print("start")
t=test()
t1=test()
t2=test()
t3=test()
print("end")  # after end t,t1,t2,t3 are the global variable which are destroy and garbage collector is called