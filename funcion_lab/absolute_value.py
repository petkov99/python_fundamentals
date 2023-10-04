number_list = input().split()
abs_values = []


for number in number_list:
    abs_values.append(abs(float(number)))


print(abs_values)
