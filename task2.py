def read_recipes(file_path):
    cook_book = {}

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        i = 0

        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1

            try:
                ingredient_count = int(lines[i].strip())
            except ValueError:
                continue

            ingredients = []

            for j in range(ingredient_count):
                i += 1
                ingredient_info = lines[i].strip().split('|')
                ingredient = {
                    "ingredient_name": ingredient_info[0].strip(),
                    "quantity": int(ingredient_info[1].strip()),
                    "measure": ingredient_info[2].strip()
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            i += 1

    return cook_book

file_path = r"C:\Users\Леша\Desktop\Git-проекты\cook_book\recipes.txt"
cook_book = read_recipes(file_path)

#for dish, ingredients in cook_book.items():
#    print(f"{dish}:")
#    for ingredient in ingredients:
#        print(f"  {ingredient['ingredient_name']}, {ingredient['quantity']}, {ingredient['measure']}")
#    print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        ingredients = cook_book.get(dish)

        if ingredients:
            for ingredient in ingredients:
                ingredient_name = ingredient["ingredient_name"]
                quantity = ingredient["quantity"] * person_count
                measure = ingredient["measure"]

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {"quantity": quantity, "measure": measure}
                else:
                    shop_list[ingredient_name]["quantity"] += quantity

        return shop_list
        
example_dishes = ["Запеченный картофель", "Омлет"]
person_count = 2
shop_list = get_shop_list_by_dishes(example_dishes, person_count)

print("Что купить:")
for ingredient, details in shop_list.items():
    print(f"{ingredient}: {details['quantity']} {details['measure']}")