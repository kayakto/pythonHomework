glas = "аеёиоуыэюя"
soglas = "йцкнгшщзхфвпрлджчсмтб"
s = input()
count_glas = 0
count_soglas = 0
for char in s:
    if char in glas:
        count_glas += 1
    elif char in soglas:
        count_soglas += 1
print(count_glas, count_soglas)