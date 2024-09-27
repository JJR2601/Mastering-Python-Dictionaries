technology_innovator = {
    'Internet': 'Tim Berners Lee',
    'Smartphone': 'Steve Jobs',
    'Personal Computer': 'Steve Wozniak',
    'Social Media': 'Mark Zuckerberg',
    'Artificial Intelligence': 'John McCarthy',
    'Blockchain': 'Satoshi Nakamoto',
    'Virtual Reality': 'Jaron Lanier',
    'Cloud Computing': 'Amazon Web Services Team'
}

print(technology_innovator)

print(technology_innovator.get('Social Media'))

technology_innovator['Smartphone'] = 'Apple Team'

technology_innovator.pop('Blockchain')

print('Cloud Computing:', technology_innovator['Cloud Computing'])
