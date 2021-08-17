
value = (500, 100, 50, 10, 5, 1)

X = int(input())
coins = []
for i in range(6):
    print("%s円: " % value[i], end='')
    coins += [int(input())]

result = 0
for i in range(6):
    add = X // value[i]
    add = coins[i] if add > coins[i] else add
    result += add
    X -= add*value[i]

print(result)
