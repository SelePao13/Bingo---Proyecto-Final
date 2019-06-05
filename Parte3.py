import random
bolillas=[random.randint(1, 15)]
i=1
while i<15:
  x=random.randint(0,15)
  for j in range(0, len(bolillas)):
    if bolillas[j]==x:
      break
  else:
    bolillas.append(x)
    i+=1
print("Las bolillas son:",bolillas)