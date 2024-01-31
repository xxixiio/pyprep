# TODO: Optimizar.
inp = input("Is perfect pyramid? ")

def check(n):
    counter = 0
    i = 0
    while counter < n:
        counter += i
        i += 1
    if (counter % n) == 0:
        return True
    else:
        return False
    
print(check(int(inp)))