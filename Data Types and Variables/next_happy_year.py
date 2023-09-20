year = int(input())
year_is_special = False

while not year_is_special:
    year += 1
    year_as_str = str(year)
    year_is_special = True
    for digit in year_as_str:
        if year_as_str.count(digit) != 1:
            year_is_special = False
            break

print(year)
