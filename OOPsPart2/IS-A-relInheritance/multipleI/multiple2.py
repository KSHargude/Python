#if both parent classes contain same method then which 
#we can write first has higher priority 
# class C(A,B)   here A has higher priority
# class C(B,A)   here B has higher priority

class A:
    def m1(self):
        print("A")               #same method m1
class B:
    def m1(self):
        print("B")
class C(A,B):                   # C(A,B)         #C(B,A)     
    def m3(self):
        print("C")
d=C()
d.m1()                          # A               # B