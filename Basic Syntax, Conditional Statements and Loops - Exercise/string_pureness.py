number = int(input())

for pure_or_not_pure_str in range(number):
    command = input()
    if ',' in command or '.' in command or '_' in command:
        print(f'{command} is not pure!')
    else:
        print(f'{command} is pure.')
