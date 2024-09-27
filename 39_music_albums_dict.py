music_albums = {
    'Thriller': '1982',
    'Back in Black': '1980',
    'The Dark Side of the Moon': '1973',
    'The Bodyguard': '1992',
    'Rumours': '1977',
    'Hotel California': '1976',
    'Nevermind': '1991',
    '21': '2011',
    'Abbey Road': '1969',
    'Lemonade': '2016'
}

print(music_albums)

print(music_albums.get('The Dark Side of the Moon'))

music_albums['21'] = 2012

music_albums.pop('Rumours')

print('Lemonade:', music_albums['Lemonade'])
