"""
class parent:
    def m1(self):
        print("parent-ma")
class child:
    def m2(self):
        print("child-m2")

p=parent()
p.m1()  #parent-m1
p.m2()  #this gives error bcoz parent cant inherit properties of child

"""

class parent:
    def m1(self):
        print("parent-ma")
class child(parent):    #######
    def m2(self):
        print("child-m2")

p=child()
p.m1()  #parent-m1
p.m2()  #child-m2