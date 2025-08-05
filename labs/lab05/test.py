import random

x = random.randint(1000,5000)
y = random.randint(1000,5000)
print(x,y)

xdamage = random.randint(0,1)
ydamage = random.randint(0,1)
print(xdamage,ydamage)



#battle
while x or y <= 0 :
 #x attack
 y = y - (x * xdamage)

 #y attack
 x = x - (y * Ydamage)

