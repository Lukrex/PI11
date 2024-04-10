ret = input("Zadaj retazec: ")
posun = int(input("Zadaj posun pre kódovanie: "))
for i in range(len(ret)):
    print(f"{ret[i]}: {ord(ret[i])}")

ret_kod = ""
for i in range(len(ret)):
    ret_kod += chr(ord(ret[i]) + posun)

print(f"Zakódovaný reťazec: {ret_kod}")
