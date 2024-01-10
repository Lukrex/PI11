while True:
    n = int(input("Zadaj N (Pre ukončenie zadaj 0): "))
    if n == 0:
        break
    print("Prvočísla:", end=" ")
    for cislo in range(2, n+1):
        pocet = 0
        for delitel in range(1, cislo+1):
            if cislo % delitel == 0:
                pocet += 1
        if pocet == 2:
            print(cislo, end=" ")
    print()
    print()