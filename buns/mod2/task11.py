numbers = input()
flag = False
existing_figure = ""
for char in numbers:
    if char == " ":
        continue
    elif char in existing_figure:
        flag = True
        break
    existing_figure += char
print(flag)
