# Define a class called Student that has the following attributes:
# name (string): the student's name
# grades (list): a list of the student's grades
# Implement methods to add grades to the student's list, calculate the student's average grade, and get the highest and lowest grades.

#1: Create a class called students w/ a name and grades attribute
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = []

            
    def add_grades(self, new_grade):
        self.grades.append(new_grade)
        print(self.grades)
        if len(self.grades) > 1:
            formatted_grades = ','.join(str(grade) for grade in self.grades)
            return formatted_grades
        else:
            return self.grades


# class Classlist:
#     def __init__(self, class_name, students):
#         self.class_name = class_name
#         self.students = {}
        
#     def add_student_to_class(self, student, grades):
#         self.students.update({student:grades})
    
    
        
        
    
add_student_grade = True
add_student_status = True 
new_student_status = True  
classroom = {}

classname = input("What is the name of the class?")

# so the program isnt quite working the way that I want to.  So I probably should go in a fix a few things
# - thinking about capitalization and bad characters; probably need to refactor and use some try and except statements instead


while add_student_status == True:
    response_to_add_student = input("Would you like to add a new student to the gradebook?").lower()
    
    if response_to_add_student == "yes":
        name = input("What is the name of the student? ")
        new_student = Student(name, grades= [])
        while add_student_grade == True:
            new_grades = int(input("What is their grade on the exam? "))
            new_student.add_grades(new_grades)
            question = input("Would you like to add another grade? Answer Yes or No ").lower()
            if question == "yes":
                print("Okay let's do that")
            else:
                print("Okay")
                classroom.update({new_student.name : new_student.grades})
                print(str(new_student.grades))
                # add_student_grade = False
                break
    else:
        print("No worries, maybe another time! Here is a list of all the students that you've created")
        # print(new_student.name + "is the name.  The scores for this student is: " + ','.join(str(grade) for grade in new_student.grades))
        add_student_status = False
    
    

print(classroom)
    # try_new_classname = input("Sorry that's not a valid name of a class, would you like to try a different name?")
    # if try_new_classname == str(try_new_classname):
            
        
    