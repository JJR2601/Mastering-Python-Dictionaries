city_landmarks = {
    'Paris': 'Eiffel Tower',
    'New York': 'Statue of Liberty',
    'Rome': 'Colosseum',
    'Sydney': 'Sydney Opera House',
    'Tokyo': 'Tokyo Tower',
    'London': 'Big Ben',
    'Cairo': 'Pyramids of Giza',
    'Rio de Janeiro': 'Christ the Redeemer'
}

print(city_landmarks)

print(city_landmarks.get('London'))

city_landmarks['New York'] = 'One World Trade Center'

city_landmarks.pop('Cairo')

print('Rio de Janeiro:', city_landmarks['Rio de Janeiro'])