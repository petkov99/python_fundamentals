budget = float(input())
price_for_1kg_flour = float(input())

price_for_pack_of_eggs = price_for_1kg_flour * 0.75
price_for_1l_milk = price_for_1kg_flour * 1.25
price_of_milk_for_1_loaf = price_for_1l_milk / 4
bread_count = 0
colored_eggs = 0
loaf_price = price_for_1kg_flour + price_for_pack_of_eggs + price_of_milk_for_1_loaf

while budget >= loaf_price:
    bread_count += 1
    budget -= loaf_price
    colored_eggs += 3

    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)


print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs "
          f"and {budget:.2f}BGN left.")


