# Define a class called Student that has the following attributes:
# name (string): the student's name
# grades (list): a list of the student's grades
# Implement methods to add grades to the student's list, calculate the student's average grade, and get the highest and lowest grades.

#1: Create a class called students w/ a name and grades attribute
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = []

        
    def get_grades(self, new_grade):
        self.grades.append(new_grade)
        return self.grades

         
name = input("What is the name of the student? ")
new_grades = int(input("What is their grade on the exam? "))
# I feel like I could create a forloop for this, which would actually be super nice...
# why do I need to specify that grades is a list when I already specified that self.grades = list?
studentA = Student(name, grades=[])
print(studentA.name) 
print(studentA.get_grades(new_grades))



#2: How to add multiple grades to the list?  


    