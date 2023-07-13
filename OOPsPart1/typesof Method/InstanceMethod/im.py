class student:
    def __init__(self,rno,nm):
        self.rollno=rno
        self.name=nm
    def info(self):
        print(f"my name is {self.name} and roll no is {self.rollno}")

s1=student(1,'abc')
s2=student(2,'pqr')
s1.info()
s2.info()