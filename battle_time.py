from colorama import Fore
import random, time, os

round = 1
winner = None
def health_stats():
  health = ((random.randint(1,6) * random.randint(1,12)) / 2) + 10
  return health
def strength_stats():
  strength = ((random.randint(1,6) * random.randint(1,12)) / 2) + 12
  return strength

print("⚔️ BATTLE TIME ⚔️")
print()
name1 = input("Name your character:\n")
name1_race = input("Choose a race (Human, Elf, Undead or Orc):\n")
print()
print(Fore.MAGENTA + name1 + Fore.RESET)
name1_health = health_stats()
name1_strength = strength_stats()
print("HEALTH: "+ Fore.RED + str(name1_health) + " HP" + Fore.RESET)
print("STRENGTH :" + Fore.YELLOW + str(name1_strength) + " ST" + Fore.RESET)
print()
print("Who are they battling?")
print()

name2 = input("Name your character:\n")
name2_race = input("Choose a race (Human, Elf, Undead or Orc):\n")
print()
print(Fore.MAGENTA + name2 + Fore.RESET)
name2_health = health_stats()
name2_strength = strength_stats()
print("HEALTH: "+ Fore.RED + str(name2_health) + " HP" + Fore.RESET)
print("STRENGTH: " + Fore.YELLOW + str(name2_strength) + " ST" + Fore.RESET)
print()
while True:
  time.sleep(3)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  difference = abs(name1_strength - name2_strength) + 1

  if dice1 > dice2:
    name2_health -= difference
    if round == 1:
      print(name1, "wins the first blow")
    else:
      print(name1, "wins round", round)
  elif dice2 > dice1:
    name1_health -= difference
    if round == 1:
      print(name2, "wins the first blow")
    else:
      print(name2, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(name1)
  print("HEALTH:", name1_health)
  print()
  print(name2)
  print("HEALTH:", name2_health)
  print()

  if name1_health <= 0:
    print(name1, "has died!")
    winner = name2
    break
  elif name2_health <= 0:
    print(name2, "has died!")
    winner = name1
    break
  else:
    print("Get ready for the next round!")
    round += 1
    

time.sleep(3)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
