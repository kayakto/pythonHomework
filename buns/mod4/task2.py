def pow_num(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num
    if n < 0:
        return 1 / pow_num(num, abs(n))
    if n % 2 == 0:
        return pow_num((num * num), n / 2)
    if n % 2 != 0:
        return num * pow_num(num, n-1)
a = int(input("Введите число, которое надо возвести в степень "))
n = int(input("Введите степень, в которую надо возвести число выше "))
print(pow_num(a, n))