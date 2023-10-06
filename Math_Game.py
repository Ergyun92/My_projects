print("Math Game")
print()
multiples = int(input("Name your multiples: "))
score = 0
for i in range(1,11):
  result = i * multiples
  print(f"{i} X {multiples} =  ")
  task = int(input("> "))
  if task == result:
    print("Great work!")
    score += 1
  else:
    print(f"Nope. The answer was {result}")
print()
print("----------------------------")
if score == 10:
  print("Fantastic! You got all of them correct 🥳")
print(f"You scored {score} out of 10")
