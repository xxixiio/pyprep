inp = int(input("Collatz Conjecture calculator. Enter a num: "))

i = 0
steps = []
while inp > 1:
    print(inp)
    i += 1
    steps.append(inp)
    if (inp % 2) == 0:
        print("x")
        inp = int(inp / 2)
    else: 
        print("y")
        inp = inp * 3 + 1
       
steps = map(str, steps)
print(f"{' -> '.join(steps)} [{i}]")