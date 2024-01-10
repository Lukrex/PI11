while True:
    cislo = int(input("Zadaj číslo (Pre ukončenie zadaj 0): "))
    pocet = 0
    if cislo == 0:
        break
    print("Delitele:", end=" ")
    for delitel in range(1, cislo+1):
        if cislo % delitel == 0:
            print(delitel, end=" ")
            pocet += 1
    print()
    print("Počet deliteľov je:", pocet)
    if pocet == 2:
        print("Číslo je prvočíslo")
    print()