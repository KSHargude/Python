class test:
    def __init__(self):
        print("constructor")
    def __del__(self):       #self is mandetory
        print("destructor")
t=test()
del t