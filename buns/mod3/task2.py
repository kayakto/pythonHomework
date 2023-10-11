a = int(input())
print("Неверный ввод" if (a < 0) else (bin(a)[2:] + ", " + oct(a)[2:] + ", " + hex(a)[2:]))