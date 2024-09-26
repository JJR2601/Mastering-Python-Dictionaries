element_symbols = {
    'Gold': 'Au',
    'Tungsten': 'W',
    'Sodium': 'Na',
    'Iodine': 'I',
    'Xenon': 'Xe',
    'Copernicium': 'Cn',
    'Radium': 'Ra',
    'Rhodium': 'Rh',
    'Gallium': 'Ga',
    'Krypton': 'Kr'
}

print(element_symbols)

print(element_symbols.get('Copernicium'))

element_symbols['Rhodium'] = 'R'

element_symbols.pop('Gallium')

print('Krypton:', element_symbols['Krypton'])