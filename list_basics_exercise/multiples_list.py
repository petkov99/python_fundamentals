factor = int(input())
count = int(input())

new_list = []

for number in range(1, count + 1):
    new_list.append(number * factor)
print(new_list)
