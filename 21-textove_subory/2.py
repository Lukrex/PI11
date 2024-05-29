fmena = open("mena.txt", "r", encoding="utf-8")
fpriezviska = open("priezviska.txt", "r", encoding="utf-8")
fmena_priezviska = open("mena_priezviska.txt", "w", encoding="utf-8")
for meno in fmena:
    priezvisko = fpriezviska.readline()
    # print(f"{meno.strip()} {priezvisko.strip()}")
    fmena_priezviska.write(f"{meno.strip()} {priezvisko.strip()}\n")

fmena.close()
fpriezviska.close()
fmena_priezviska.close()