car_specs = {
    'toyota camry': '3.5L V6',
    'ford f-150': '3.3L V6',
    'nissan altima': '2.0L VC-Turbo l4',
    'bmw 3 series': '3.0L l6 Turbo',
    'mercedes-benz c-class': '3.0L l6 Turbo',
    'hyundai sonata': '1.6L Turbo l4',
    'kia sorento': '2.5L l4',
    'audi a4': '2.0L l4 Turbo',
    'honda accord': '1.5L Turbo l4',
    'chevrolet silverado 1500': '4.3L V6'
}

print(car_specs)

print(car_specs.get('bmw 3 series'))

car_specs['honda accord'] = '2.0L Turbo l4'

car_specs.pop('mercedes-benz c-class')

print('chevrolet silverado 1500:', car_specs['chevrolet silverado 1500'])