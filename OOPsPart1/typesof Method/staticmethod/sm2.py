class student:
    @staticmethod
    def add(num1,num2):
        print(num1+num2)

student.add(10,20)
s1=student()
s1.add(10,20)

"""
class student:
    def add(num1,num2):
        print(num1+num2)

student.add(10,20)
s1=student()
s1.add(10,20)

o/p   30
    error  bcoz def add(num1=self, num2=10)   then 20 where
"""