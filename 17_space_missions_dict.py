space_missions = {
    'sputnik 1': '1957',
    'voyager 1': '1977',
    'ISS': '1998',
    'mars exploration rover': '2003',
    'change 4': '2018',
    ''
}

print(space_missions)

print(space_missions.get('ISS'))

space_missions['voyager 1'] = '2000'

space_missions.pop('mars exploration rover')

print('change 4:', space_missions['change 4'])

