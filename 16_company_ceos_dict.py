company_ceo = {
    'amazon': 'andy jassy',
    'microsoft': 'satya nadella',
    'google': 'sundar pichai',
    'tesla': 'elon musk',
    'facebook': 'mark zuckerberg',
    'intel': 'patrick gelsinger',
    'oracle': 'safra catz',
    'apple': 'tim cook',
    'amd': 'lisa tzwu-fang su',
    'yahoo': 'jim lanzone'
}

print(company_ceo)

print(company_ceo.get('intel'))

company_ceo['google'] = 'Ruth Porat'

company_ceo.pop('amd')

print('yahoo:', company_ceo['yahoo'])