
N = input()
W = input()
n = int(N)
all_set = []
for i in range(n):
    value = input()
    all_set.append(value)


exist: bool = False
bit = 0
while bit < (1 << n):
    sum = 0
    for i in range(n):
        sum += int(all_set[i])

    if sum == int(W):
        exist = True
    bit += 1


if exist:
    print("yes")
else:
    print("no")
