dog_breed = {
    'chihuahua': 'small',
    'french bulldog': 'small',
    'yorkshire terrier': 'small',
    'beagle': 'medium',
    'shiba inu': 'medium',
    'australian shepherd': 'medium',
    'labrador retriever': 'large',
    'german shepherd': 'large',
    'golden retriever': 'large',
    'rottweiler': 'large',
}

print(dog_breed)

print(dog_breed.get('shiba inu'))

dog_breed['german shepherd'] = 'great dane'

dog_breed.pop('australian shepherd')

print('rottweiler:', dog_breed['rottweiler'])

