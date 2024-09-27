coffee_types = {
    'Espresso': 'A strong and concentrated coffee brewed by forcing hot water through finely-ground coffee',
    'Americano': 'Espresso diluted with hot water for a milder flavor',
    'Latte': 'Espresso mixed with steamed milk and topped with foam',
    'Cappuccino': 'Equal parts espresso, steamed milk, and milk foam',
    'Macchiato': 'Espresso topped with a small amount of milk or milk foam',
    'Mocha': 'A chocolate-flavored variant of a latte',
    'Flat White': 'A strong coffee with a higher ratio of coffee to milk',
    'Affogato': 'A scoop of vanilla ice cream topped with a shot of hot espresso',
    'Ristretto': 'A short shot of espresso, using less water for a bolder flavor',
    'Cold Brew': 'Coffee brewed with cold water over an extended period'
}

print(coffee_types)

print(coffee_types.get('Cappuccino'))

coffee_types['Affogato'] = 'A dessert of ice cream drowned in espresso'

coffee_types.pop('Macchiato')

print('Cold Brew:', coffee_types['Cold Brew'])
