job_salaries = {
    'Software Engineer': '₱38,099',
    'Nurse': '₱32,101',
    'Teacher': '₱21,473',
    'Civil Engineer': '₱24,181',
    'Accountant': '₱31,100',
    'Marketing Manager': '₱22,784',
    'Data Scientist': '₱50,489',
    'Graphic Designer': '₱24,865',
    'Sales Executive': '₱22,000',
    'Research Scientist': '₱29,708'
}

print(job_salaries)

print(job_salaries.get('Teacher'))

job_salaries['Data Scientist'] = '₱50,000'

job_salaries.pop('Sales Executive')

print('Research Scientist:', job_salaries['Research Scientist'])
