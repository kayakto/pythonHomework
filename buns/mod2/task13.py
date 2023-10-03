barcode = input()
acceptable_barcode = ""
odd_pozition = 0
even_pozition = 0
index = 1
for char in barcode:
    if index % 2 == 1:
        odd_pozition += int(char)
    else:
        even_pozition += int(char)
    index += 1

sum = str(odd_pozition + (3 * even_pozition))

if sum[-1] == "0":
    print("yes")
else:
    print("no")