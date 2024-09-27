space_telescopes = {
    'Hubble Space Telescope': 'Observing distant galaxies',
    'Chandra X-ray Observatory': 'Studying high-energy regions',
    'James Webb Space Telescope': 'Observing the early universe',
    'Kepler Space Telescope': 'Searching for exoplanets',
    'Spitzer Space Telescope': 'Infrared observations of celestial objects'
}

print(space_telescopes)

print(space_telescopes.get('James Webb Space Telescope'))

space_telescopes['Hubble Space Telescope'] = 'Exploring the cosmos'

space_telescopes.pop('Kepler Space Telescope')

print('Spitzer Space Telescope:', space_telescopes['Spitzer Space Telescope'])