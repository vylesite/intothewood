#!/bin/python3


# Topic 2 Part 2
# Exercise 2.2
# best way
mark = None
while (mark == None):
    try:
        mark = int(input("Enter your grade: "))
    except:
        print("Not a number!")

    grade = ""
    if (mark >= 0 and mark <= 100):
        if (mark < 50):
            grade = "Fail"
        elif (mark < 60):
            grade = "Pass"
        elif (mark < 70):
            grade = "Credit"
        elif (mark < 80):
            grade = "Distinction"
        elif (mark <= 100):
            grade = "High Distinction"
    else:
        grade = "Mark outside of range"

    print(grade)






