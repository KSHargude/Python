class A:
    def m1(self):
        print("A")
class B(A):
    def m2(self):
        print("B")
class C(B):
    def m3(self):
        print("C")
class D(C):
    def m4(self):
        print("D")
#1
d=D()
d.m1()   #A
d.m2()   #B
d.m3()   #C
d.m4()   #D

#2
#  d=A()
#  d.m1()    A
#  d.m2()    error
#  d.m3()
#  d.m4()

#3
#  d=B()
#  d.m1()    A
#  d.m2()    B
#  d.m3()    error
#  d.m4()

#4
#  d=C()
#  d.m1()    A
#  d.m2()    B
#  d.m3()    C
#  d.m4()    error










