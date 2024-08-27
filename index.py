x = input("Zadejte proměnou x: ") #Input = vstup (ptá se uživatelé, co má do x uložit)
y = input("Zadejte proměnou y: ")

#Přetypovává na int (číslo)
x = int(x)
y = int(y)

print("Zde máte možnosti: ")
print(" Pro sčítání zadejte +")
print(" Pro odčítání zadejte -")
print(" Pro násobení zadejte *")
print(" Pro dělení zadejte /")
print(" Pro mocnění zadejte **, x = mocněnec a y = mocnitel")
print(" Pro odmocenění zadejte /*, x = odmocněnec a y = odmocnitel")

znamenko = input("Zadejte vaší volbu operátoru: ")

#Zde provádím porovnávání, program zjišťuje, co zadal uživatel
if znamenko == "+":
  #Zde se provede sčítání
  print(x+y)
#Pokud chci v podmínce pokračovat, nedávám if, ale elif (jestli že)
elif znamenko == "-":
  print(x-y)
elif znamenko == "/":
  #Jestliže chci dále něco kontrolovat, mohu podmínky vnořovat
  if y == 0:
    #Nesmíte zapomenout, že python chce mít odsazený kód
    print("Nelze dělit nulou")
  else:
    print(x/y)
elif znamenko == "*":
  print(x*y)
elif znamenko == "**":
  print(x**y)
elif znamenko == "/*":
  if y<0:
    print(x**(1/y))