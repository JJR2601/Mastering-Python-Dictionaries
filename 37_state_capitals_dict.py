state_capitals = {
    'pennsylvania': 'harrisburg',
    'georgia': 'atlanta',
    'washington': 'olympia',
    'new york': 'albany',
    'illinois': 'springfield',
    'florida': 'tallahassee',
    'texas': 'austin',
    'ohio': 'columbus',
    'michigan': 'lansing',
    'california': 'sacramento'
}

print(state_capitals)

print(state_capitals.get('new york'))

state_capitals['michigan'] = 'michigan'

state_capitals.pop('texas')

print('california:', state_capitals['california'])