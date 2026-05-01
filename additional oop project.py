class Student:
    def __init__(self,name,grades):
        self.name=name
        self.__grades=grades

    def add_grade(self,grade):
        self.__grades.append(grade)
        print(f"Grade {grade} added for {self.name}")

    def get_average(self):
        average=sum(self.__grades)/len(self.__grades)
        return average
    
    def introduce(self):
        average = self.get_average()
        print(f"Hi I am {self.name} and my average grade is {average}")
    

student=Student("Michael",[])
student.add_grade(89)
student.add_grade(90)
student.add_grade(88)
student.add_grade(86)
student.introduce()
        