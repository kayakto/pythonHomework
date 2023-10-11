domain = input().split(".")
first, second, third = map(str, reversed(domain))
print(first + "\n" + second + "\n" + third)