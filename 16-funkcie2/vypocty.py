def sucet(x, y):
    return x + y


def parne(cislo):
    if cislo % 2 == 0:
        return "párne"
    else:
        return "nepárne"


def prvocislo(cislo):
    prvocis = True
    for i in range(2, cislo):
        if cislo % i == 0:
            prvocis = False
    return prvocis


a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))
sucet = sucet(a, b)
print(f"Súčet čísel {a} + {b} = {sucet}")
print(f"Číslo {a} je {parne(a)}")
print(f"Číslo {b} je {parne(b)}")
if prvocislo(a) == True:
    print(f"Číslo {a} je prvočíslo!")
else:
    print(f"Číslo {a} nie je prvočíslo!")
if prvocislo(b) == True:
    print(f"Číslo {b} je prvočíslo!")
else:
    print(f"Číslo {b} nie je prvočíslo!")
