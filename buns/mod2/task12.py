telephone_number = input()
acceptable_values = "+0123456789"
acceptable_telephone_number = ""
for char in telephone_number:
    if char in acceptable_values:
        acceptable_telephone_number += char
print(acceptable_telephone_number)
