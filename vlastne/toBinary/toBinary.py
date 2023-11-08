res = [0,0,0,0,0,0,0,0]
i = 0
inp = int(input("Enter a number: "))
while(inp != 0):
    res[0 + i] = inp % 2
    inp = inp // 2
    i += 1
print(res[7],res[6],res[5],res[4],res[3],res[2],res[1],res[0])