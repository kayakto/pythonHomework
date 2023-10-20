def nod(a,b):
    if a == 0 or b==0:
        return max(a,b)
    else:
        max_n = max(a,b)
        min_n = min(a,b)
        return nod(max_n % min_n, min_n)
a, b = map(int, input("Введите два числа через пробел ").split())
print("НОД =", nod(a,b))