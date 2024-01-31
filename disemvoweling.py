inp = input("No vowels. Input: ")

no_vowel = ""
for i in range(len(inp)):
    char = inp[i]
    if char.lower() in ["a", "e", "i", "o", "u"]:
        no_vowel += "*"
    else:
        no_vowel += char
        
print(no_vowel)