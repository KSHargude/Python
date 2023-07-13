class student:
    def __init__(self,rno,nm):
        self.rollno=rno
        self.name=nm

s1=student(1,'abc')
s2=student(2,'pqr')
s1.age=20
s2.rollno=5
print(s1.rollno,s1.name,s1.age)
#  print(s1.rollno,s1.name,s1.age)  gives error bcoz age not present