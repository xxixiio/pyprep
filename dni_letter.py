inp = input("DNI to calc a the letter: ")

letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
remainder = int(inp) % 23

print(inp + letters[remainder])