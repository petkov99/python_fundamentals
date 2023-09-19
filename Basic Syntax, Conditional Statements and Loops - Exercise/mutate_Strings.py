first_str = input()
second_str = input()
last_printed_str = first_str

for character_index in range(len(first_str)):
    left_part = second_str[:character_index + 1]
    right_part = first_str[character_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_str:
        print(new_string)
        last_printed_str = new_string
