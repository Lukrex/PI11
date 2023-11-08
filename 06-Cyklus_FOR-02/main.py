# premenna i je pocitadlo pre cyklus
# range nam vrati postupnost cisiel od 0 po N-1
# range moze mat aj viac parametrov - prvy je od, druhy je pokial-1, a treti je skok
# priklad range(2, 11, 2) vypise cisla 2,4,6,8,10

# n = int(input("Zadaj n: "))
# sucet = 0
# for i in range(1, n+1):
#     print(i)
#     sucet += i
# print("Súčet čísiel od 1 do", n, "je", sucet)

n = int(input("Zadaj n: "))
faktorial = 1
for i in range(1, n+1):
    faktorial = faktorial * i
print(n, "! =", faktorial)