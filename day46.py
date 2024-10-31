title = "MokeBeast"
print(f"{title: ^60}")
print()


beast = {}


def prettyPrint():
  print()
  for key, value in beast.items():
      print(key, end=": ")
      for subkey, subvalue in value.items():
          print(subkey, subvalue, end=" | ")
      print()

while True:
  name = input("beast name > ")
  element = input("beast element > ")
  move = input("Special Move > ")
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  beast[name] = {"Name": name, "Element": element, "Move": move, "HP": hp, "MP": mp}
  prettyPrint()
  print()
  print()
  again = input("Again? y/n > ")
  if again == "y":
      print()
      continue
  else:
      print("Thank you for playing")
      break