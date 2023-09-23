start_index = int(input())
final_index = int(input())

for char in range(start_index, final_index + 1):
    asci_char = chr(char)
    print(asci_char, end=' ')