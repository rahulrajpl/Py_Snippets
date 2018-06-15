# Print a formatted price list with a given width

width = input('Please enter width:')

price_width=10
item_width=width-price_width

header_format='%s*s%*s'
format='%s*s%*.2f'

print('=' * width)

print(header_format % (item_width,'Item',price_width,'Price'))
print('-' * width)

print(format % (item_width, 'Apples', price_width, 0.4))

print('=' * width)