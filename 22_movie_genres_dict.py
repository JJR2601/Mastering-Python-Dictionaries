movie_genre = {
    'comedy': 'kung fu hustle',
    'adventure': 'raiders of the lost ark',
    'horror': 'train to busan',
    'mystery': 'prometheus',
    'sci-fi': 'interstellar',
    'thriller': 'zodiac',
    'drama': 'titanic',
    'fantasy': 'game of thrones'
}

print(movie_genre)

print(movie_genre.get('horror'))

movie_genre['sci-fi'] = 'the martian'

movie_genre.pop('drama')

print('fantasy:', movie_genre['fantasy'])

