festival_dates = {
    'sinulog festival': '3rd sunday of january',
    'dinagyang festival': '4th sunday of january',
    'ati-atihan festival': '3rd sunday of january',
    'panagbenga festival': 'whole february',
    'kadayawan festival': '3rd week august',
    'masskara festival': '4th sunday of october',
    'giant lantern festival': 'december 17',
    'moriones festival': 'holy week',
    'pintados-kasadayan festival': 'june 29',
    'kaamulan festival': 'second half of february'
}

print(festival_dates)

print(festival_dates.get('ati-atihan'))

festival_dates.pop('kadayawan festival')

print('kaamulan festival:', festival_dates['kaamulan festival'])