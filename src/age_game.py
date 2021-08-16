print('start game!!')
left: int = 20
right: int = 36

while right - left > 1:
    mid: int = left + (right - left) // 2
    print('Is the age less than %d ? (yes/no)' % (mid))
    ans = input()
    if ans == 'yes':
        right = mid
    else:
        left = mid

print("The age is %d" % left)
