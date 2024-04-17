import json

with open("ingredients.json") as f:
    ingredients = json.load(f)


drinks = []
on = True
while on:
    drink = {
        "name": '',
        "ingredients": {},
        "mixed": '',
        "tags": []
    }

    drink['name'] = input("Name of drink: ")

    editIngredients = True
    while editIngredients:
        ingred, amount, unit = input("Enter ingredient and amount ").split('/')
        
        if ingred not in ingredients.keys():
            print("invalid ingredient")
            continue
        drink['ingredients'][ingred] = {"amount": float(amount), "unit": unit}

        if input("continue? ") != '':
            editIngredients = False

    drink['mixed'] = input("shaken/stired lol ")

    tmp = []
    for ingred in drink['ingredients']:
        tmp += ingredients[ingred]['tags']
    drink['tags'] = list(set(tmp))

    if input("quit? ") != '':
        on = False

with open("drinks.json") as f:
    read = json.load(f)
with open("drinks.json", 'w') as f:
    write = json.dump(read.update(drinks))