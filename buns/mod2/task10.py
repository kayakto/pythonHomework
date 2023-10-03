s = input()
word = ""
last_char = ""

for char in s:
    if char == ' ':
        if last_char != "":
            word += last_char
        last_char = ""
    else:
        last_char = char
if last_char != "":
    word += last_char

print(word)