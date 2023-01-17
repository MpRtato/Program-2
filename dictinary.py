#vardnica
Cipari = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 5000, 'M': 1000}

Ciparikey = Cipari.keys()

#ievade
print("Ievadi skaitli: ")

while 1 > 0:
  inp = input("> ")

  inpm = []
  for i in inp:
    inpm.append(i)

  pinpm = []
  for i in inpm:
    if i in Ciparikey:
      pinpm.append(i)

  if len(inpm) == len(pinpm):
    break

print(inpm)

#vertiegusana
for i in inpm:
  Ciparival = Cipari.get(i)
  print(Ciparival)

#for i in inpm:
