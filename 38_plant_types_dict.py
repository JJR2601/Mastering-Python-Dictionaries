plant_types = {
    'oak': 'tree',
    'rose': 'shrub',
    'basil': 'herb',
    'cactus': 'succulent',
    'maple': 'tree',
    'lavender': 'herb',
    'aloe vera': 'succulent',
    'hydrangea': 'shrub'
}

print(plant_types)

print(plant_types.get('maple'))

plant_types['rosel'] = 'plant'

plant_types.pop('lavender')

print('hydrangea:', plant_types['hydrangea'])