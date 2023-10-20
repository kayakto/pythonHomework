def check_array(array):
    if len(set(array)) == 1:
        return "Все числа равны"
    different_num_arr = []
    all_num_equal = True
    for num in array:
        if num in different_num_arr:
            all_num_equal = False
            break
        else:
            different_num_arr.append(num)
    if all_num_equal:
        return "Все числа разные"
    return "Есть равные и неравные числа"
arrayChar = input("Введите список чисел через пробел: ").split()
array = list(map(int, arrayChar))
print(check_array(array))


