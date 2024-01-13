heights = "151 145 179"

# Input a Python list of student heights
student_heights = heights.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
students = 0
total_height = 0
for i in student_heights:
  students += 1
  total_height += i

print(f"total height = {total_height}")
print(f"number of students = {students}")
print(f"average height = {round(total_height/students)}")