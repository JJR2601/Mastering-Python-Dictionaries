beach_locations = {
    'Boracay Beach': 'Philippines',
    'Bondi Beach': 'Australia',
    'Copacabana': 'Brazil',
    'Maya Bay': 'Thailand',
    'Waikiki Beach': 'USA',
    'Ipanema Beach': 'Brazil',
    'Playa del Carmen': 'Mexico',
    'Anse Source d Argent': 'Seychelles'
}

print(beach_locations)

print(beach_locations.get('Copacabana'))

beach_locations['Ipanema Beach'] = 'Rio de haneiro'

beach_locations.pop('Waikiki Beach')

print('Anse Source d Argent:', beach_locations['Anse Source d Argent'])
