# Define a class called Student that has the following attributes:
# name (string): the student's name
# grades (list): a list of the student's grades
# Implement methods to add grades to the student's list, calculate the student's average grade, and get the highest and lowest grades.

#1: Create a class called students w/ a name and grades attribute
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

            
    def add_grades(self, new_grade):
        self.grades.append(new_grade)
        print(self.grades)
        if len(self.grades) > 1:
            formatted_grades = ','.join(str(grade) for grade in self.grades)
            return formatted_grades
        else:
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
    
    
# class Classlist:
#     def __init__(self, class_name, students):
#         self.class_name = class_name
#         self.students = {}
        
#     def add_student_to_class(self, student, grades):
#         self.students.update({student:grades})
    
    
        
new_class = True   
add_student_grade = True
add_student_status = True
user_score_options = True   
classroom = {}


while new_class == True:
    classname = input("What is the name of the class?")
    if not classname.isalpha():
        print("The name needs to be alphabet letters only")
        break
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
                classroom.update({new_student.name : new_student.grades})
                question = input("Would you like to add another grade? Answer Yes or No ").lower()
                if question == "yes":
                    print("Okay let's do that")
                else:
                    print("Okay")
                    print(classroom)
                    print(str(new_student.grades))
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
            if len(classroom) == 0:
                print("This should exit the program")
                # new_class = False
                # add_student_status = False
            else:
                for student, grade in classroom.items():
                    print(student + " is the student's name and their grades are: " + ','.join(str(x) for x in grade))                
            new_class = False
            add_student_status = False
                
            
    
# teacher level --> class (math/english) --> students --> grades
# writing to files to act like a database =) using json
            