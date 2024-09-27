festival_locations = {
    'Sinulog Festival': 'Cebu City',
    'Pahiyas Festival': 'Lucban, Quezon',
    'Kadayawan Festival': 'Davao City',
    'Panagbenga Festival': 'Baguio City',
    'Ati-Atihan Festival': 'Kalibo, Aklan',
    'Obando Fertility Rites': 'Obando, Bulacan',
    'Bangus Festival': 'Dagupan City',
    'Viva Vigan Binatbatan Festival': 'Vigan City'
}

print(festival_locations)

print(festival_locations.get('Panagbenga Festival'))

festival_locations['Obando Fertility Rites'] = 'Bulacan'

festival_locations.pop('Pahiyas Festival')

print('Bangus Festival:', festival_locations['Bangus Festival'])
