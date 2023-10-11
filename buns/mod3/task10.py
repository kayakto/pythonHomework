size = int(input())
for column in range(1, size+1):
    for row in range(1, size+1):
        if row != size:
            print(row, end=", ")
        else:
            print(row)

print()

for column in range(1, size+1):
    for row in range(1, size+1):
        if row != size:
            print(column, end=", ")
        else:
            print(column)
