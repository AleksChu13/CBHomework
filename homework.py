"""Книга рецептов(словарь)
"""
def get_cook_book():
    cook_book = {}
    name_key = ['ingredient_name', 'quantity', 'measure']
    with open('menu.txt', encoding='utf-8') as file:
        for line in file:
            cook_book[line.strip()] = []
            ingredients_quantity = int(file.readline())
            for ingredient in range(ingredients_quantity):
                ingredient_list = file.readline().strip().split(' | ')
                cook_book[line.strip()] += [dict(zip(name_key, ingredient_list))]
            file.readline()
    return cook_book

# pprint(get_cook_book())





""" Дополнение (кол-во ингредиентов)
"""


def get_shop_list_by_dishes(dishes, person):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in cook_book.keys():
        for name_dish in dishes:
            if dish == name_dish:
                get_ingredient_list(shop_list, cook_book[dish], person)

    return shop_list


def get_ingredient_list(shop_list, dish, person):
    for ingredient in dish:
        ingredient_name = ingredient['ingredient_name']
        measure = ingredient['measure']
        quantity = int(ingredient['quantity']) * person
        if len(shop_list) == 0:
            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            quantity = get_new_quantity(shop_list, quantity, ingredient_name)
            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def get_new_quantity(shop_list, quantity, ingredient):
    ingredients_list = shop_list.keys()
    for ingredient_name in ingredients_list:
        if ingredient_name == ingredient:
            ingredient_dict = shop_list[ingredient]
            new_quantity = ingredient_dict['quantity'] + quantity
            return new_quantity
    return quantity

# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

""" Сортировка строк
"""

def get_len_file(file_name, files_list):
    with open(file_name, encoding='utf-8') as document:
        quantity = 0
        for _ in document:
            quantity += 1
        files_list += [quantity]


def get_sort_files(files):
    files_list = []
    for file_name in files:
        get_len_file(file_name, files_list)
    files_tuple = list(zip(files, files_list))
    files_tuple.sort(key=lambda quantity: quantity[1])
    return files_tuple


def deleted_data(new_file):
    with open(new_file, 'w', encoding='utf-8') as doc:
        doc.seek(0)


def get_rewrite_file(files, new_file):
    deleted_data(new_file)
    files_tuple = get_sort_files(files)
    for file in files_tuple:
        with open(new_file, 'a', encoding='utf-8') as new_doc, open(file[0], 'r', encoding='utf-8') as doc:
            new_doc.write(f'{file[0]} \n')
            new_doc.write(f'{str(file[1])} \n')
            for line in doc:
                new_doc.write(line)
            new_doc.write(f'\n')


get_rewrite_file(['1.txt', '2.txt', '3.txt'], 'result.txt')