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

print("------------------------------------------------")
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# sorted_scores = sorted(student_scores)
#
# print(f"The highest score in the class is: {sorted_scores[-1]}")

# or

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


