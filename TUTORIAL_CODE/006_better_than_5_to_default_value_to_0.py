from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print('Red:     %r' % red)
# Red:     '5'
print('Green:   %r' % green)
# Green:   0
print('Opacity: %r' % opacity)
# Opacity: 0

# OR

red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

print('Red:     %r' % red)
# Red:     5
print('Green:   %r' % green)
# Green:   0
print('Opacity: %r' % opacity)
# Opacity: 0
