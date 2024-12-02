print ("Examination Grade Calculator")

#The grading scale
#70-100 == A
#60-69 == B
#51-59 == C
#45-50 == D
#40-44 == E
#0-39 == F
crying_face = '\U0001F622'
heart = '\U0001F496'   

# Get user input
course =input("Name of Exam:")
maxScore= int(input("What is the maximum possible score?:"))
score_of_student = int(input("What is your score?:"))

# Calculate the percentage in two decimal places
student_percent = score_of_student / maxScore * 100
student_percent= round (student_percent,2)

if student_percent <=100 and student_percent>=70:
    print ("Your score is",student_percent,"and you got an A")
    print ("Good job, Keep it up!",heart)
elif student_percent <=69 and student_percent>=60:
    print ("Your score is",student_percent,"and you got a B")
    print ("Nice try!,A little more effort and you will get to the top!")
elif student_percent <=59 and student_percent>=51:
    print ("Your score is",student_percent,"and you got a C")
    print ("You did well but you can do better. I believe in you!")
elif student_percent <=50 and student_percent>=45:
    print ("Your score is",student_percent,"and you got a D")
    print ("You need to try harder!")
elif student_percent <=44 and student_percent>=40:
    print ("Your score is",student_percent,"and you got an E")
    print ("Narrow escape. Its not too late to improve!")
else:
    print ("Your score is",student_percent,"and you got an F")
    print ("You failed",course,crying_face)