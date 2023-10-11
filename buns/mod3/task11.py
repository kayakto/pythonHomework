def Cross_Zero(first_str,second_str, third_str):
    board = [first_str, second_str, third_str]
    for stroke in board:
        if stroke[0] == stroke[1] and stroke[0] == stroke[2] and (stroke[0] == "X" or stroke[0] == "O"):
            return stroke[0]
    for i in range(len(board)):
        if first_str[i] == second_str[i] and first_str[i] == third_str[i] and (third_str[i] == "O" or third_str[i] == "X"):
            return first_str[i]
    if first_str[0] == second_str[1] and second_str[1] == third_str[2] and (third_str[2] == "O" or third_str[2] == "X"):
        return first_str[0]
    elif first_str[2] == second_str[1] and second_str[1] == third_str[0] and (third_str[0] == "O" or third_str[0] == "X"):
        return first_str[2]
    else:
        return "Ничья"
first_str = input()
second_str = input()
third_str = input()
print(Cross_Zero(first_str,second_str, third_str))
