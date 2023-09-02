import os, time
inventory = []

try:
    with open("inventory.txt", "r") as f:
        inventory = eval(f.read())
except:
    print("No inventory found")


def addItem():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    item = input("What would you like to add > ").capitalize()
    inventory.append(item)
    print("Item added")


def removeItem():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    item = input("What would you like to remove > ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print("Item removed")
    else:
        print("You don't have that")


def viewItem():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    seen = set(inventory)
    for item in seen:
        print(f"{item} {inventory.count(item)}")


while True:
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    menu = input("1: Add\n2: View\n3: Remove\n> ")
    if menu == "1":
        addItem()
    elif menu == "2":
        viewItem()
    else:
        removeItem()

    with open("inventory.txt", "w") as f:
        f.write(str(inventory))

