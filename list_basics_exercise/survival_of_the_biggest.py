number_str = input().split()
numbers = []

for num in number_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(', '.join(map(str, numbers)))



