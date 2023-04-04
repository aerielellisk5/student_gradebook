# Define a class called Student that has the following attributes:
# name (string): the student's name
# grades (list): a list of the student's grades
# Implement methods to add grades to the student's list, calculate the student's average grade, and get the highest and lowest grades.

#1: Create a class called students w/ a name and grades attribute
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = []

    # def get_student_name():
    #     name = input("What is the name of the student? ")
    #     return name
            
    def get_grades(self, new_grade):
        self.grades.append(new_grade)
        return self.grades


class Classlist:
    def __init__(self, class_name, students):
        self.class_name = name
        self.students = {}
        
    def add_new_classname():
        classname = input("What is the name of the class?")
    
    def add_new_student():
        name = input("What is the name of the student? ")
    

        
        
        
        
add_student = True    
# classname = input("What is the name of the class?")             
# name = input("What is the name of the student? ")
# new_grades = int(input("What is their grade on the exam? "))
# I feel like I could create a forloop for this, which would actually be super nice...
# why do I need to specify that grades is a list when I already specified that self.grades = list?
# studentA = Student(name, grades=[])
# print(studentA.name) #prints out the name 
# print(studentA.get_grades(new_grades)) #prints out the grade




#2: How to add multiple grades to the list?  
# probably need to somehow ask all the questions and put it in an if statement?

while add_student:
    classname = input("What is the name of the class?")
    # might be better to make this a function? 
    name = input("What is the name of the student? ")
    new_grades = int(input("What is their grade on the exam? "))
    question = input("Would you like to add another grade? Answer Yes or No ")
    if question == "No":
        print("All done")
        break
    else:
        continue
    
    # try_new_classname = input("Sorry that's not a valid name of a class, would you like to try a different name?")
    # if try_new_classname == str(try_new_classname):
            
        
    


studentA = Student(name, grades=[])

print(studentA.name) #prints out the name 
print(studentA.get_grades(new_grades)) #prints out the grade

    