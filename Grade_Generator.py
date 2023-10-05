print("Grade Generator")
print()
exam = input("Name of the exam: ")
max_score = int(input("Max possible score: "))
your_score = int(input("Your score: "))
percentage = float(max_score * (your_score / 100))
percentage = round(percentage, 2)
if 100 >= percentage >= 90:
  print(f"You've got {percentage}% which is an A+")
elif 89 >= percentage >= 80:
  print(f"You've got {percentage}% which is an A")
elif 79 >= percentage >= 70:
  print(f"You've got {percentage}% which is a B")
elif 69 >= percentage >= 60:
  print(f"You've got {percentage}% which is a C")
elif 59 >= percentage >= 50:
  print(f"You've got {percentage}% which is a D")
else:
  print(f"You've got {percentage}% which is U")
