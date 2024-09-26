app_rating = {
    'wikipedia': '4.5',
    'telegram': '4.1',
    'spotify': '4.3',
    'facebook': '4.6',
    'steam': '2.2',
    'threads': '4.4',
    'capcut': '4.1',
    'zoom': '4.0',
    'canva': '4.7',
    'crunchyroll': '4.2'
}

print(app_rating)

print(app_rating.get('threads'))

app_rating['zoom'] = '4'

app_rating.pop('canva')

print('crunchyroll:', app_rating['crunchyroll'])