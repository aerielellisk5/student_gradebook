# Define a class called Student that has the following attributes:
# name (string): the student's name
# grades (list): a list of the student's grades
# Implement methods to add grades to the student's list, calculate the student's average grade, and get the highest and lowest grades.

#1: Create a class called students w/ a name and grades attribute

import jsonpickle
import os

class Student:
    # might need to add class here so that the student can keep track of the class that they are in easier?
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

            
    def add_grades(self, new_grade):
        self.grades.append(new_grade)
        # print(self.grades)
        if len(self.grades) > 1:
            formatted_grades = ','.join(str(grade) for grade in self.grades)
            return formatted_grades
        else:
            return self.grades
        
    def get_student_grades(self):
        return self.grades
        
    def average_grade(self, grades):
        if len(grades) > 1:
            total = 0
            for i in grades:
                total = total + i
            average = total/len(grades)
        else:
            average = grades
        return int(average)
    
    def highest_grade(self, grades):
        high_grade = 0
        if len(grades) > 1:
            for i in grades:
                if i > high_grade:
                    high_grade = i
                else:
                    continue
        else:
            high_grade = grades
        return int(high_grade)
    
    def lowest_grade(self, grades):
        if len(self.grades) > 1:
            lowest_grade = 100 
            for i in grades:
                if i < lowest_grade:
                    lowest_grade = i
                else:
                    continue
        else:
            lowest_grade = grades        
        return int(lowest_grade)
    
    # Should be able to pull what classes each student is in and then which students are in each class (ideally)
class Classlist:
    def __init__(self, classname, students):
        self.classname = classname
        self.students = students
        
    def add_student(self, student):
        self.students.append(student)
            
    def show_classlist(self):
        students_name = []
        for student in self.students:
            # students_name.append(student.name)
            print(student.name)
            print("show me the grade")
            print(student.get_student_grades())
        # print(students_name)
        
filename = "classlist.json"
if os.stat(filename).st_size == 0:
    print("File is empty")
else:
    with open("classlist.json", "r") as file:
        data = file.read()       
        database_data = jsonpickle.decode(data)
        file.close()
        # to get access to the student data I need to use a for loop
        for student in database_data.students:
            print(student.name)
            print(student.grades)




no_selection = True      
new_class = True   
add_student_grade = True
add_student_status = True
user_score_options = True   
# classroom = {}

while no_selection:
    class_type = input("Would you like to add a student to a new class, or an existing class? Please type new or existing, or q to quit ")
    if class_type == "q":
        print("Exiting the program")
        exit()
    elif "new" not in class_type and "exist" not in class_type:
        print(class_type)
        print("That doesn't seem like a valid answer, try again")
        continue
    elif "new" in class_type:
        no_selection = False
        # print("new here")
        classname = input("What is the name of the class you would like to add the student to? ")
        current_class = Classlist(classname, [])
    elif "exist" in class_type:
        print("exists here")
        no_selection = False
        current_class_name = input("Which class would you like to add a student to? ")
        # so currently I can save the data to another file, and then bring it back to this file, so that's good.  I need to edit this part to make sure check and see if the class that is entered already exists, and then make sure that I add additional info to that specific object.
        if current_class_name  == database_data.classname:
            current_class = database_data
        
    while add_student_status == True:
        add_student_grade = True
        response_to_add_student = input("Would you like to add a new student to the gradebook?").lower()
        if response_to_add_student == "yes":
            user_score_options = True
            name = input("What is the name of the student? ")
            new_student = Student(name, [])
            while add_student_grade == True:
                new_grades = int(input("What is their grade on the exam? "))
                new_student.add_grades(new_grades)
                current_class.add_student(new_student)    

                question = input("Would you like to add another grade? Answer Yes or No ").lower()
                if question == "yes":
                    print("Okay let's do that")
                else:
                    print("Okay")
                    current_class.show_classlist()

                    while user_score_options:
                        score_options = input("Would you like to see the average, highest or lowest score for this student?")
                        if score_options.lower() == "average":
                            print(new_student.average_grade(new_student.grades))
                        elif score_options.lower() == "highest":
                            print(new_student.highest_grade(new_student.grades))
                        elif score_options.lower() == "lowest":
                            print(new_student.lowest_grade(new_student.grades))
                        else:
                            print("No worries, let's head back to the top of the loop.")
                            add_student_grade = False
                            user_score_options = False
                            continue
        
        else:
            print("No worries, maybe another time!")
            # if len(current_class) == 0:
            #     print("This should exit the program")
                # new_class = False
                # add_student_status = False
            # else:
            #     for student, grade in current_class.items():
            #         print(student + " is the student's name and their grades are: " + ','.join(str(x) for x in grade))                
            new_class = False
            add_student_status = False
            

with open("classlist.json", "w") as file:
    file.write(jsonpickle.encode(current_class))
    
file.close()
            


            
# serialized_obj = jsonpickle.encode(current_class)
# print(serialized_obj)
    
# loaded_classlist = jsonpickle.decode(serialized_obj)
# print(loaded_classlist.classname)

# teacher level --> class (math/english) --> students --> grades
# writing to files to act like a database =) using json
        