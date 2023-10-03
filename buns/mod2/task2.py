def round_number(number, n):
    multiplier = 10 ** n
    rounded_number = int(number * multiplier + 0.5) / multiplier
    rounded_number = str(rounded_number)

    counter = 0
    for char in rounded_number:
        if char == '.':
            if rounded_number[counter+1] == '0' and rounded_number[counter+1] == rounded_number[-1]:
                rounded_number += '0'
                break
        counter += 1
    return rounded_number

side_of_square = float(input())
perimeter_of_square = side_of_square * 4
square_area = side_of_square ** 2
diagonal_of_square = side_of_square * 2 ** 0.5
print(round_number(perimeter_of_square, 2), round_number(square_area, 2), round_number(diagonal_of_square, 2))