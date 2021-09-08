class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printVal(self):
        print("name",self.name)
        print("age",self.age)

class Employee(Person):
    def __init__(self,job,salary,name,age):
        super().__init__(name,age)
        self.job=job
        self.salary=salary
    def printv(self):
        print("job",self.job)
        print("salary",self.salary)

emp=Employee("dev",50000,"amal",32)
emp.printVal()
emp.printv()
