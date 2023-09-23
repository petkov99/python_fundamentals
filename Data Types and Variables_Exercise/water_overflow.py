number_of_lines = int(input())
tank_size = 255
capacity = 0

for i in range(number_of_lines):
    liter_of_water = int(input())
    if liter_of_water > tank_size:
        print("Insufficient capacity!")
        continue
    capacity += liter_of_water
    tank_size -= liter_of_water
print(capacity)