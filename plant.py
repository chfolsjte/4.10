a = '*'     #a = *號

for i in range(1,13,2):     # i 從1開始 間隔2個 到13 有 1,3,5,7,9,11

    print("{0:^11s}".format(a*i)) #有11隔空格可以讓a*i值放入 ^:置中的意思
for i in range(9,0,-2):
    print("{0:^11s}".format(a*i))
