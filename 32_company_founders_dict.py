company_founders = {
    'apple inc': 'steve jobs',
    'microsoft corp': 'bill gates',
    'amazon inc': 'jeff bezos',
    'facebook inc': 'mark zuckerberg',
    'google llc': 'larry page',
    'tesla inc': 'martin eberhard',
    'netflix inc': 'reed hastings',
    'linkedin': 'reid hoffman',
}

print(company_founders)

print(company_founders.get('tesla inc'))

company_founders['microsoft corp'] = 'paul allen'

company_founders.pop('linkedin')

print('linkedin:', company_founders['linkedin'])