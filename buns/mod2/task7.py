s = input()
count_zero = 0
count_one = 0

for char in s:
    if char == "1":
        count_one += 1
    else:
        count_zero += 1
if count_one == count_zero:
    print("yes")
else:
    print("no")