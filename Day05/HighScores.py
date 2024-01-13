input = "78 65 89 86 55 91 64 89"
# Input a list of student scores
student_scores = input.split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
x = None
for i in student_scores:
  if not x or x < i:
    x = i

print(f"The highest score in the class is: {x}")