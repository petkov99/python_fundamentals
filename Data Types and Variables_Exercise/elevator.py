from math import ceil

persons_to_elevate = int(input())
capacity = int(input())

courses = ceil(persons_to_elevate / capacity)
print(courses)