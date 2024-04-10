inp = input("Zadaj: ")

samoh = 0
ostatne = 0
for i in range(len(inp)):
    if inp[i] in "aeiyouýáíéóúä":
        print(inp[i], " je samohláska")
        samoh += 1
    else:
        print(inp[i], "nie je samohláska")
        ostatne += 1

print(f"\nSamohlások je {samoh} a ostatných charakterov je {ostatne}")