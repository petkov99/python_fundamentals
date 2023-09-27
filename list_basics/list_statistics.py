numbers = int(input())
positive = []
negative = []

for _ in range(numbers):
    num = int(input())
    if num >= 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
print(positive)
print(negative)
print(f'Count of positives:', len(positive))
print(f'Sum of negatives:', sum(negative))

