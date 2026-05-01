class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old")

    
class Student(Person):
    def study(self,course):
        print(f"{self.name} is studying {course}")

class Employee(Person):
    def work(self,company):
        print(f"{self.name} works at {company}")



student=Student("Michael", 17, )
employee=Employee("Yaa" , 24 ,)   

student.introduce()
student.study("Biology")
employee.introduce()
employee.work("AffiliMike")

        


