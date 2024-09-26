animal_habitats = {
    'lion': 'savanna',
    'polar bear': 'arctic',
    'giraffe': 'woodlands',
    'dolphin': 'oceans',
    'kangaroo': 'grasslands',
    'fox': 'forests',
    'clown fish': 'coral reefs',
    'frog': 'tropical rainforests'
}

print(animal_habitats)

print(animal_habitats.get('giraffe'))

animal_habitats['kangaroo'] = 'scrub lands'

animal_habitats.pop('clown fish')

print('frog:', animal_habitats['frog'])