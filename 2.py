z = 5
x = 2 * z - 2
for i in range(0, z):
    for j in range(0, x):
        print(' ', end='')
    x -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
