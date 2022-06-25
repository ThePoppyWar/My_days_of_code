student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(round(sum(student_heights) / len(student_heights)))

# or

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heigts = 0
for heigts in student_heights:
  sum_heigts += heigts
print(sum_heigts)



number_of_student = 0
for student in student_heights:
  number_of_student += 1
print(number_of_student)

print(round(sum_heigts/number_of_student))




