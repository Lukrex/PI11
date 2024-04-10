retazec = input("Zadaj string: ")
print(retazec)

for i in range(len(retazec)):
    print(i, retazec[i])

print("\n")

for i in range(1, len(retazec)+1):
    print(-i+(len(retazec)), retazec[-i])
