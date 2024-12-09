for i in range(0, 8):
    print(i)
    if i == 8:
        break

    print(" ")

for i in range(0, 9, 1):
    if i == 8 or i == 9:
        print(i)
    else:
        pass

        print("")

for i in range(10):
    if i % 2 == 0:
        print(i)

print(" ")

for n in range(10):
    if n % 2 == 0:
        continue
    else:
        print(n)
