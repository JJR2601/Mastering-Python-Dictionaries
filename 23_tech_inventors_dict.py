tech_inventors = {
    'telephone': 'alexander graham bell',
    'light bulb': 'thomas edison',
    'printing press': 'johannes gutenberg',
    'television': 'philo farnsworth',
    'sewing machine': 'elias howe',
    'camera': 'george eastman'
}

print(tech_inventors)

print(tech_inventors.get('television'))

tech_inventors['light bulb'] = 'joseph swan'

tech_inventors.pop('camera')

print('camera:', tech_inventors['camera'])