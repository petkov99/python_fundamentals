numbers = input().split()
list_numbers = list(map(int, numbers))
min_number = min(list_numbers)
max_number = max(list_numbers)
sum_number = sum(list_numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_number}")
