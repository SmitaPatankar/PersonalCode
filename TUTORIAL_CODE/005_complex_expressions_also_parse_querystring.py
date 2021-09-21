from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)

print(repr(my_values))
# {'red': ['5'], 'blue': ['0'], 'green': ['']}
print('Red:     ', my_values.get('red'))
# Red:      ['5']
print('Green:   ', my_values.get('green'))
# Green:    ['']
print('Opacity: ', my_values.get('opacity'))
# Opacity:  None
