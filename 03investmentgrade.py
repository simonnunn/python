# Name    : 07Examgrade

# Author  : Simon Nunn

# Date    : 04 July 2018

# Purpose : Exam Grade

def exam_grade(level,mark):
    if level < 1 or level > 4:
        print("Invalid level")
    elif mark < 0 or mark > 100:
        print("Invalid mark")
    elif level == 1 or level == 2:
        if mark >= 85:
            print("Distinction")
        elif mark >= 75:
            print("Merit")
        elif mark >= 65:
            print("Pass")
        else:
            print("Fail")
    elif level == 3:
        if mark >= 80:
            print("Distinction")
        elif mark >= 70:
            print("Merit")
        elif mark >= 60:
            print("Pass")
        else:
            print("Fail")
    elif level == 4:
        if mark >= 70:
            print("Distinction")
        elif mark >= 60:
            print("Merit")
        elif mark >= 50:
            print("Pass")
        else:
            print("Fail")
            
# main code

level = int(input("Please enter level: "))
mark  = int(input("Please enter mark : "))

exam_grade(level,mark)

