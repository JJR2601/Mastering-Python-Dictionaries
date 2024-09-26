holiday_dates = {
    'christmas': 'december 25',
    'all saints day': 'november 1',
    'all souls day': 'november 2',
    'new years eve': 'january 1',
    'national heroes day': 'august 26',
    'ninoy aquino day': 'august 21',
    'rizal day': 'december 30',
    'bonifacio day': 'november 30',
    'labor day': 'may 1',
    'day of valor': 'april 9'

}

print(holiday_dates)

print(holiday_dates.get('new years eve'))

holiday_dates['labor day'] = 'may 2'

holiday_dates.pop('all saints day')

print('day of valor:', holiday_dates['day of valor'])