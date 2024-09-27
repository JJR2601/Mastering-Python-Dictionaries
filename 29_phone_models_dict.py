phone_models = {
    'iphone': 'apple',
    'samsung': 'samsung',
    'google pixel': 'google',
    'oneplus': 'oneplus',
    'asus rog phone': 'asus',
    'vivo': 'vivo',
    'cherry mobile': 'cosmic',
    'nokia': 'nokia',
    'xiaomi': 'xiaomi',
    'tecno mobile': 'tecno'
}

print(phone_models)

print(phone_models.get('samsung'))

phone_models['nokia'] = 'nokia corp'

phone_models.pop('cherry mobile')

print('tecno mobile:', phone_models['tecno mobile'])
