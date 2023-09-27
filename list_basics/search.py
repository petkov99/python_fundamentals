numbers = int(input())
word = input()
my_list = []
filtered_list = []

for _ in range(numbers):
    words = input()
    my_list.append(words)
    if word in words:
        filtered_list.append(words)

print(my_list)
print(filtered_list)