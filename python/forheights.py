student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students = 0
total_height = 0

for std in student_heights:
    total_height += std
    students += 1

print(round(total_height / students))
