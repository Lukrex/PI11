# import math >> o = 2 * math.pi * r
# import math as matematika >> o = 2 * matematika.pi * r
# from math import * >> o = 2 * pi * r
from math import pi

import random

r = 10
o = 2 * pi * r
print(round(o, 2))

cislo = random.randrange(0, 10)
farba = random.choice(["red", "green", "blue"])
print(cislo)
print(farba)
