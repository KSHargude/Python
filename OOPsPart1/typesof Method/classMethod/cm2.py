#####imp

class student:
    count=0
    def __init__(self):
        student.count=student.count+1
    @classmethod
    def display(cls):
        print(cls.count)
s1=student()
s2=student()
student.display()
s3=student()
student.display()