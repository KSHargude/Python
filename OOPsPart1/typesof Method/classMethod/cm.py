#  @classmethod  deporator

class student:
    cname='cpt'
    @classmethod
    def cinfo(cls):
        print(f"college name is {cls.cname} and thiscollege started in 2002")

s1=student()
s2=student()
student.cinfo()
s1.cinfo()
         