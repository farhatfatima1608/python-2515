#Student Grade Tracker

student_id=input("Enter student id:")
student_name=input("Enter student name:")
student_attendence = int(input("Enter student attendance: "))


total_score=0
number_of_score=0

continue_input="Yes"

while continue_input=="Yes":
    current_score = int(input(f"Enter score {number_of_score+1}: "))

    continue_input=input("Do you want to continue(Yes/No)")
    number_of_score+=1
    total_score=total_score+current_score

print (number_of_score)
print(total_score)

#Average score 
average_score= total_score/number_of_score

#Grade the student 
if average_score>=85:
    print("A")
elif average_score>=70:
    print("B")
elif average_score>=50:
    print("C") 
else:
    print("Fail")


#Attendence Criteria 
attendence_status = "WARNING LOW ATTENDENCE" if int(student_attendence) < 75 else "OK GOOD ATTENDENCE"


print("Student Name:"+student_name)
print("Student Total Score:", total_score)
print("Student Number of score:", number_of_score)
print("Student Average score:", average_score)
print("Student Attendence Status:", attendence_status)


# Award eligibility 
if average_score >= 85 and student_attendence > 75:
    print("Got Awarded")


