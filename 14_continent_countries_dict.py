continent_countries = {
    'asia': {'japan', 'philippines', 'indonesia'},
    'africa': {'nigeria', 'ethiopia', 'egypt'},
    'north america': {'united states', 'canada', 'mexico'},
    'south america': {'brazil', 'argentina', 'chile'},
    'europe': {'united kingdom', 'germany', 'france'},
    'australia': {'australia', 'new zealand', 'papua new guinea'}
}

print(continent_countries)

print(continent_countries.get('south america'))

continent_countries['europe'] = {'poland', 'romania', 'netherlands'}

continent_countries.pop('australia')

print('australia:', continent_countries['australia'])