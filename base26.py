inp = input("Base26: ")

if inp.isdigit():
    print("from decimal to base26")
else:
    base26 = inp.upper()[::-1]
    counter = 0
    for i in range(len(base26)):
        num = int(ord(base26[i]) - 64)
        counter += num * pow(26, i)
    print(counter)