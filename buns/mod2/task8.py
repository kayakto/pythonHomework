str_and_symbol = input()
i = str_and_symbol[-1]
s = str_and_symbol[:-2]
count_i = 0
for char in s:
    if char == i:
        count_i += 1
    else:
        break
print(count_i)

