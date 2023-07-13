class A:
    def m1(self):
        print("A")
class B:
    def m2(self):
        print("B")
class C(A,B):
    def m3(self):
        print("C")

#1
d=C()
d.m1()   #A
d.m2()   #B
d.m3()   #C

#2
#  d=A()
#  d.m1()    A
#  d.m2()    error
#  d.m3()

#2
#  d=B()
#  d.m2()    A
#  d.m1()    error
#  d.m3()
