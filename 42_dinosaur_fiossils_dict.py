dinosaur_fossils = {
    'Tyrannosaurus Rex': 'North America',
    'Triceratops': 'North America',
    'Velociraptor': 'Mongolia',
    'Brachiosaurus': 'North America',
    'Stegosaurus': 'North America',
    'Ankylosaurus': 'North America',
    'Spinosaurus': 'North Africa'
}

print(dinosaur_fossils)

print(dinosaur_fossils.get('Brachiosaurus'))

dinosaur_fossils['Triceratops'] = 'USA and Canada'

dinosaur_fossils.pop('Ankylosaurus')

print('Spinosaurus:', dinosaur_fossils['Spinosaurus'])
