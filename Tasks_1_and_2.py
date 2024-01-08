from pprint import pprint


def create_dict(data):
    """Функция создания словаря с рецептами по данным, считанным из файла"""

    lines_amount = len(data)
    current_line_number: int = 0
    cook_book = {}

    while current_line_number <= lines_amount:

        dish = data[current_line_number].split()
        current_line_number += 1

        ingredients_amount = int(data[current_line_number])
        current_line_number += 1

        ingredients_list = []
        for item in range(current_line_number, current_line_number + ingredients_amount):
            new_ingredient = {}
            ingredient_line = data[item].strip().split(' | ')
            new_ingredient['ingredient_name'] = ingredient_line[0]
            new_ingredient['quantity'] = ingredient_line[1]
            new_ingredient['measure'] = ingredient_line[2]
            ingredients_list.append(new_ingredient)

        cook_book[' '.join(dish)] = ingredients_list

        current_line_number += ingredients_amount + 1

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """Функция подсчета необходимого количества ингредиентов в зависимости от выбранных блюд и количества человек"""

    necessary_ingredients_amount = {}

    for recipe in dishes:

        ingredients = recipe_book[recipe]
        for item in range(len(ingredients)):

            current_ingredient = ingredients[item]
            current_ingredient_amount = int(current_ingredient["quantity"]) * person_count

            if current_ingredient["ingredient_name"] in necessary_ingredients_amount.keys():
                necessary_ingredients_amount[current_ingredient["ingredient_name"]]["quantity"] \
                    += current_ingredient_amount
            else:
                necessary_ingredients_amount[current_ingredient["ingredient_name"]] \
                    = {'measure': current_ingredient["measure"],
                       "quantity": current_ingredient_amount}

    return necessary_ingredients_amount


with open('recipes.txt', 'r', encoding='utf-8') as f:
    file_data = f.readlines()

recipe_book = create_dict(file_data)

persons = 2
buying_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], persons)
pprint(buying_list)


