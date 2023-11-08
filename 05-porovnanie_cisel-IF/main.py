"""
a, b, c = int(input("Zadaj číslo a: ")), int(input("Zadaj číslo b: ")), int(input("Zadaj číslo c: "))

if a == b == c:
    print("Čísla sa rovnajú")
else:
    if a > b:
        if a > c:
            print("Najväčšie číslo je", a)
        else:
            print("Najväčšie číslo je", c)
    else:
        if b > c:
            print("Najväčšie číslo je", b)
        else:
            print("Najväčšie číslo je", c)
"""

a, b, c = int(input("Zadaj číslo a: ")), int(input("Zadaj číslo b: ")), int(input("Zadaj číslo c: "))
d, e = int(input("Zadaj číslo d: ")), int(input("Zadaj číslo e: "))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print("Najvačšie číslo je", max)