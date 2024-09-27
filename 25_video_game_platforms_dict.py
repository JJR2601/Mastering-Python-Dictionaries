video_game_plaforms = {
    'minecraft': 'console',
    'the legend of zelda': 'nintendo switch',
    'gta v': 'xbox',
    'pokemon go': 'ios',
    'wild rift': 'android',
    'tetris': 'game boy',
    'pac-man': 'arcade',
    'league of legends': 'windows'

}
print(video_game_plaforms)

print(video_game_plaforms.get('the legend of zelda'))

video_game_plaforms['tetris'] = 'windows'

video_game_plaforms.pop('pokemon go')

print('league of legends:', video_game_plaforms['league of legends'])