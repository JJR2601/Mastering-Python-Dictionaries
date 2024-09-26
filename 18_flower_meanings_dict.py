flower_meaning = {
    'chrysantemum': 'slighted love',
    'daisy': 'innocence',
    'lily': 'purity',
    'peony': 'passion',
    'rose': 'love',
    'sunflower': 'adoration',
    'daffodil': 'regard',
    'aster': 'faith'
}

print(flower_meaning)

print(flower_meaning.get('rose'))

flower_meaning['daffodil'] = 'unequalled love'

flower_meaning.pop('sunflower')

print('aster:', flower_meaning['aster'])

