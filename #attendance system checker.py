#attendance system checker
'''
step 1:get the total number of students
step 2: get the attendance of each student
step 3: check if the attendance is less than 75%
'''
n=int (input("Enter the number of students: "))
attendance = []
for i in range(n):
    a = int(input(f"Enter the attendance of student {i+1}: "))
    attendance.append(a)

for i in range(n):
    if attendance[i]<75:
        print(r"Student {i+1} has less than 75% attendance: {attendance[i]}%")
    elif attendance[i] >= 75:
        print(f"Student {i+1} has sufficient attendance: {attendance[i]}% and is eligible for exams.")
    
    if attendance[i] not in range(0, 100):

        print(f"Invalid attendance for student {i+1}: {attendance[i]}%")