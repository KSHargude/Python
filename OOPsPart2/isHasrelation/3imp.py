#if we are creating child class object and child class doesnt cpntain 
#constructor then parent class constructor will be executed but parent class object will not be created

class parent:
    def __init__(self):
        print ("constructor")
        print(id(self))

class child(parent):
    pass

c=child()
print(id(c))