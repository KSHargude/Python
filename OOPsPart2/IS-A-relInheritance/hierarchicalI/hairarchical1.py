class A:
    def m1(self):
        print("A")
class B(A):
    def m2(self):
        print("B")
class C(A):
    def m3(self):
        print("C")

#1
d=A()
d.m1()   #A
d.m2()   #error
d.m3()   

#2
#  d=B()
#  d.m1()    A
#  d.m2()    B
#  d.m3()    error

#2
#  d=C()
#  d.m1()    A
#  d.m3()    C
#  d.m3()    error
