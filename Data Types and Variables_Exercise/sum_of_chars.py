number_of_lines = int(input())
total_sum = 0

for char in range(number_of_lines):
    current_char = input()
    asci_char = ord(current_char)
    total_sum += asci_char

print(f'The sum equals: {total_sum}')
