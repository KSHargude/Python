class student:
    cname='cpt'
    def __init__(self,rno,nm):
        self.rollno=rno
        self.name=nm

s1=student(1,'abc')
s2=student(2,'pqr')
s1.cname='csd'
print(s1.rollno,s1.name,s1.cname) #instance
print(s2.rollno,s2.name,s2.cname)

print(s1.rollno,s1.name,student.cname) #static