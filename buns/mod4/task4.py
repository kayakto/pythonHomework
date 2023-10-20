user_string = input("Введите слово ")
if len(user_string) % len(set(user_string)) == 0:
    print(''.join(set(user_string)) + ''.join(set(user_string))[::-1])
elif (len(user_string)-1) % (len(set(user_string))-1) == 0:
    simbol_frequency = []
    for elem in set(user_string):
        simbol_frequency.append([user_string.count(elem), elem])
    simbol_frequency.sort(reverse=True)
    polindrom = ''
    for i in range(len(simbol_frequency)):
        polindrom += simbol_frequency[i][1]
    polindrom = polindrom + polindrom[::-1]
    polindrom = polindrom.replace(simbol_frequency[-1][1], '', 1)
    print(polindrom)