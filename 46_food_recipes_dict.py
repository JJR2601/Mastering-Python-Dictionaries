food_recipes = {
    'Spaghetti': 'Boil pasta, add sauce, and mix',
    'Pizza': 'Prepare dough, add toppings, and bake',
    'Sushi': 'Roll rice and fillings in seaweed',
    'Tacos': 'Fill tortillas with meat and vegetables',
    'Burgers': 'Grill patties, add buns and toppings',
    'Salad': 'Mix greens, veggies, and dressing',
    'Soup': 'Simmer ingredients in broth',
    'Curry': 'Cook spices and vegetables in sauce'
}

print(food_recipes)

print(food_recipes.get('Burgers'))

food_recipes['Sushi'] = 'Prepare rice, roll with fillings and seaweed'

food_recipes.pop('Soup')

print('Curry:', food_recipes['Curry'])
