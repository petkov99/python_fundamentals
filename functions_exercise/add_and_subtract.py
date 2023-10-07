def sum_numbers(first, second):
    returned_result = first + second
    return returned_result


def subtract(returned_result, third):
    sub_result = returned_result - third
    return sub_result


def add_and_subtract(first, second, third):
    add = sum_numbers(first, second)
    subtraction = subtract(add, third)
    return subtraction


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))