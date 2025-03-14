print("Vítejte v programu Kalkulačka")

while True:
  x = int(input("Zadejte proměnnou x: "))
  y = int(input("Zadejte proměnnou y: "))

  """

  x = int(x)
  y = int(y)

  """
  print("Zde máte na výběr z následující nabídky: ")
  print("1. Sčítání zadejte - 1")
  print("2. Odčítání zadejte - 2")
  print("3. Násobení zadejte - 3")
  print("4. Dělení zadejte - 4")
  print("5. Mocnění zadejte - 5")
  print("6. Odmocnění zadejte - 6")
  print("0. Konec programu - ")

  operator = input("Zadejte volbu matematické operace: ")

  if operator == "1":
    print(x+y)
  elif operator == "2":
    print(x-y)
  elif operator == "3":
    print(x*y)
  elif operator == "4":
    if y != 0:
      print(x/y)
    else:
      print("Nejsi Chuck Norris")
  elif operator == "5":
    print(x**y)
  elif operator == "6":
    # <> - pravý alt + , a .
    if x > 0:
      print(x**(1/y))
    else:
      print("Nemůžete odmocňovat záporná čísla")
  elif operator == "0":
    break
  else:
    print("Nezvolil jsi správné číslo")