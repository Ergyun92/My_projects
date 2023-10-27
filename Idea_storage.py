import time, random, os

print("🌟Idea Storage🌟")
print()

def add():
  os.system("clear")
  print("Write down your idea")
  idea = input("> ")
  f = open("my.idea", "a+")
  f.write(f"{idea}\n")
  print("Nice! Your idea has been stored.")
  time.sleep(1)
  os.system("clear")
  f.close()

def view():
  os.system("clear")
  f = open("my.idea", "r")
  read = f.read().split("\n")
  read.remove("")
  f.close()
  r_idea = random.choice(read)
  print(r_idea)
  time.sleep(3)
  os.system("clear")

while True:
  menu = input("Do you want to add an idea or to view a random one?(a/v): ")
  if menu == 'a':
    add()
  else:
    view()
