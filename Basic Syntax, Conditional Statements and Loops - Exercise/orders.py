number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100.0:
        continue
    if days < 1 or days > 31:
        continue
    if caps_per_day < 1 or caps_per_day > 2000:
        continue

    coffee = price_per_capsule * days * caps_per_day
    total_price += coffee
    print(f'The price for the coffee is: ${coffee:.2f}')

print(f'Total: ${total_price:.2f}')

