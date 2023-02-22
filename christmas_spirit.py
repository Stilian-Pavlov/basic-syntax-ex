quantity_of_decoration = int(input())
days_until_christmas = int(input())
spirit = 0
day = 1
ornament_set_price = 2
ornament_set_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17
total_price = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decoration += 2

    if day % 2 == 0:
        total_price += ornament_set_price * quantity_of_decoration
        spirit += ornament_set_spirit

    if day % 3 == 0:
        total_price += tree_skirt_price * quantity_of_decoration + tree_garland_price * quantity_of_decoration
        spirit += tree_skirt_spirit + tree_garland_spirit

    if day % 5 == 0:
        total_price += tree_lights_price * quantity_of_decoration
        spirit += tree_lights_spirit

    if day % 15 == 0:
        spirit += 30

    if day % 10 == 0:
        spirit -= 20
        total_price += 23

        if day == days_until_christmas:
            spirit -= 30


print(f"Total cost: {total_price}")
print(f"Total spirit: {spirit}")
