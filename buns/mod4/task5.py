input_file = input("Ведите имя файла ")
with open(input_file, 'r', encoding='UTF-8') as file:
    read_file = file.read()
count_symbol = []
for char in set(read_file):
    if char.isalpha():
        count_symbol.append([read_file.count(char), char])
count_symbol.sort()
with open('output.txt', 'w', encoding='UTF-8') as file:
    for pair in count_symbol:
        file.write(f"{pair[1]}: {pair[0]}\n")


