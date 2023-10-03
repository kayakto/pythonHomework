numbers = input()
len_a = 0
len_b = 0
counter_found_numbers = 0
for char in numbers:
    if char == ' ':
        counter_found_numbers += 1
    if counter_found_numbers == 0:
        len_a += 1
    elif counter_found_numbers == 1:
        len_b += 1

a = int(numbers[:len_a])
b = int(numbers[len_a + 1: len_a + len_b])
c = int(numbers[len_b + len_a + 1:])

if ((a >= b) and (b >= c)) or ((c >= b) and (b >= a)):
    print(b)
elif ((b >= a) and (a >= c)) or ((c >= a) and (a >= b)):
    print(a)
else:
    print(c)



