sports_event = {
    'Milo Marathon': '2023',
    'PBA Finals': '2022',
    'UAAP Basketball Championship': '2023',
    'Philippine Southeast Asian Games': '2023',
    'Rugby World Cup Sevens': '2022',
    'MMA Fight Night': '2024',
    'Ironman 70.3': '2023'
}

print(sports_event)

print(sports_event.get('UAAP Basketball Championship'))

sports_event['MMA Fight Night'] = '2025'

sports_event.pop('Rugby World Cup Sevens')

print('Ironman 70.3:', sports_event['Ironman 70.3'])
