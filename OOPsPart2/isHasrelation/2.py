class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(self.name,self.age)

class car:
    def __init__(self,model):
        self.model=model

class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
        self.car=car("fd")

    def info(self):
        self.show()
        print(self.name,self.age,self.salary)

e=Employee("abc",20,30000)
e.info()