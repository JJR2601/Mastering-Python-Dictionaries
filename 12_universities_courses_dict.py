university_course = {
    'Harvard': 'Law',
    'MIT': 'Computer Science',
    'UP': 'Business Administration',
    'UST': 'Medicine',
    'PUP': 'IT',
    'CLSU': 'Agriculture',
    'Saint Louis University': 'Engineering',
    'University of the Cordilleras': 'Criminology'
}

print(university_course)

print(university_course.get('UP'))

university_course['pup'] = 'Education'

university_course.pop('Saint Louis Universities')

print('University of the Cordilleras', university_course['University of the Cordilleras'])