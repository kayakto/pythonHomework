site_name = input()
len_third = 0
len_second = 0
counter_found_domains = 0
for char in site_name:
    if char == '.':
        counter_found_domains += 1
    if counter_found_domains == 0:
        len_third += 1
    elif counter_found_domains == 1:
        len_second += 1
third_domain = site_name[:len_third]
second_domain = site_name[len_third + 1: len_third + len_second]
first_domain = site_name[len_second + len_third + 1:]
print(first_domain)
print(second_domain)
print(third_domain)
