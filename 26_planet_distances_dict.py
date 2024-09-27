planet_distances = {
    'mercury': '57 million km',
    'venus': '108 million km',
    'earth': '150 million km',
    'mars': '228 million km',
    'jupiter': '779 million km',
    'saturn': '1,434 billion km',
    'uranus': '2,872 billion km',
    'neptune': '4,495 billion km'
}

print(planet_distances)

print(planet_distances.get('earth'))

planet_distances['jupiter'] = '780 million km'

planet_distances.pop('uranus')

print('neptune:', planet_distances['neptune'])
