software_version = {
    '.net framework': '.net framework 4.8.1',
    'windows 11': 'version 23h2',
    'adobe photoshop': 'version 25.0',
    'zoom': 'version 5.15.0',
    'google chrome': 'chrome 118.0.5993.90',
    'microsoft edge': '129.0.2792.52'
}

print(software_version)

print(software_version.get('zoom'))

software_version['windows 11'] = '22h2'

software_version.pop('google chome')

print('microsoft edge:', software_version)



