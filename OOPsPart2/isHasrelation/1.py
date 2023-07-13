class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class car:
    def __init__(self,model):
        self.model=model

class Employee(person):
    def __init__(self,name,age,salary,car):
        super().__init__(name,age)
        self.salary=salary
        self.car=car

    def info(self):
        print(self.name,self.age,self.salary)
        print(self.car.model)

c=car("xyz")
e=Employee("abc",20,30000,c)
e.info()