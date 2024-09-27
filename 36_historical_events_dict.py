historical_events = {
    'french revolution': '1789',
    'world war 1': '1914',
    'world war 2': '1939',
    'spanish colonization': '1565',
    'apollo 11': '1969',
    'philippine-american war': '1899-1902',
    'japanese occupation': '1942',
    'super typhoon yolanda': '2013'
}

print(historical_events)

print(historical_events.get('world war 1'))

historical_events['japanese occupation'] = '1942-1945'

historical_events.pop('apollo 11')

print('super typhoon yolanda:', historical_events['super typhoon yolanda'])