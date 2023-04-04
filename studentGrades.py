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
            # print(formatted_grades)
            return formatted_grades
        else:
            return self.grades


class Classlist:
    def __init__(self, class_name, students):
        self.class_name = name
        self.students = {}
        
    def add_new_classname():
        classname = input("What is the name of the class?")
    
    def add_new_student():
        name = input("What is the name of the student? ")
    

        
        
        
        
add_student_status = True 
new_student_status = True   
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


# classname = input("What is the name of the class?")
while add_student_status == True:
    response_to_add_student = input("Would you like to add a new student to the gradebook?") 
    if response_to_add_student == "yes":
        name = input("What is the name of the student? ")
        new_student = Student(name, grades= [])
        while new_student_status == True:
            new_grades = int(input("What is their grade on the exam? "))
            new_student.add_grades(new_grades)
            question = input("Would you like to add another grade? Answer Yes or No ")
            if question == "No":
                print("Okay")
                print(str(new_student.grades))
                new_student_status = False
            else:
                continue
    else:
        print("No worries, maybe another time! Here is a list of all the students that you've created")
        print(new_student.name + "is the name.  The scores for this student is: " + ','.join(str(grade) for grade in new_student.grades))
        add_student_status = False
    
    
    # try_new_classname = input("Sorry that's not a valid name of a class, would you like to try a different name?")
    # if try_new_classname == str(try_new_classname):
            
        
    


# # studentA = Student(name, grades=[])

# print(studentA.name) #prints out the name 
# print(studentA.get_grades(new_grades)) #prints out the grade

    