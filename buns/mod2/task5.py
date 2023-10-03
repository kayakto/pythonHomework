alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol_and_number = input()
i = symbol_and_number[0]
n = int(symbol_and_number[2:])
index_i = 0
counter = 0
for char in alphabet:
    if char == i:
        index_i = counter
        break
    counter += 1
index_k = index_i + n
print(alphabet[index_k])

