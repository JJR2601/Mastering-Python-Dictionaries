artist_songs = {
    'marshmello': 'happier',
    'avicii': 'wake me up',
    'coldplay': 'hymn for the weekend',
    'ed sheeran': 'thinking out loud',
    'alan walker': 'faded',
    'thefatrat': 'unity',
    'twenty one pilots': 'stressed out',
    'bruno mars': 'just the way you are',
    'mark ronson': 'uptown funk',
    'wiz khalifa': 'see you again'
}

print(artist_songs)

print(artist_songs.get('coldplay'))

artist_songs['thefatrat'] = 'monody'

artist_songs.pop('bruno mars')

print('wiz khalifa:', artist_songs['wiz khalifa'])