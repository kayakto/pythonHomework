numbers = input()
a = 0
b = 0
index_separator = 0
for char in numbers:
    if char == ",":
        a = int(numbers[: index_separator])
        b = int(numbers[index_separator + 2:])
        break
    index_separator += 1
c = a % b
print(c)

