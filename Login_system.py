from replit import db
import os, random, time

print("🌟Login System🌟")

def add_user():
  os.system("clear")
  name = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if name in keys:
    print("Error: Username already exists")
    return
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[name] = {"password": newPassword, 
              "salt": salt}
  time.sleep(1)
  print("Details stored")

def log_in():
  os.system("clear")
  name = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if name not in keys:
    print("Error: Username doesn't exists")
    return
  salt = db[name]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[name]["password"] == newPassword:
    print("Logged in successfuly")
  else:
    print("Wrong username or password")

while True:
  menu = int(input("1. Add User\n2. Login\n> "))
  if menu == 1:
    add_user()
  elif menu == 2:
    log_in()
  else:
    print("Invalid command")
