layer = 5

for i in range(1, layer + 1):
    for j in range(layer - i):
        print(' ', end = "")

    for j in range(i):
        print('*', end = "")
        
    print("")