def is_armstrong_number(num):
    num_str = str(num)
    p = len(num_str)
    sum_of_powers = sum(int(digit) ** p for digit in num_str)
    return num == sum_of_powers

def armstrong_numbers_generator():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1

generator = armstrong_numbers_generator()

def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
