def calculate(operator, first_number, second_number):
    if operator == 'add':
        return first_number + second_number
    elif operator == 'subtract':
        return first_number - second_number
    elif operator == 'multiply':
        return first_number * second_number
    elif operator == 'divide':
        return int(first_number / second_number)


input_operator = input()
first_num = int(input())
second_num = int(input())
result = calculate(input_operator, first_num, second_num)
print(result)
