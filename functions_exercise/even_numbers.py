def is_even(number):
    return number % 2 == 0


numbers_as_string = input().split()
numbers_as_digits = []

for number in numbers_as_string:
    numbers_as_digits.append(int(number))
even_numbers = []

for element in numbers_as_digits:
    if is_even(element):
        even_numbers.append(element)
print(even_numbers)
