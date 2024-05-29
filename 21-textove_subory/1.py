fmena = open("mena.txt", "r", encoding="utf-8") # otvori subor mena na citanie / r->citanie w->zapis
# fmena = open("C:/dokumenty/mena.txt", "r")

while True:
    riadok = fmena.readline()
    if riadok == "":
        break
    print(riadok[:-1]) # [:-1] vypise znaky od nulteho po predposledny


fmena.close() # treba zatvorit subor vzdy