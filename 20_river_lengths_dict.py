river_lengths = {
    'amazon river': '6,575 km',
    'mississippi river': '6,275 km',
    'congo river': '4.700 km',
    'mackenzie river': '4,241 km',
    'nile river': '6,650 km',
    'yangtze river': '6,300 km'
}

print(river_lengths)

print(river_lengths.get('mississippi river'))

river_lengths['nile river'] = '6,700 km'

river_lengths.pop('mackenzie river')

print('yangtze river:', river_lengths['yangtze river'])