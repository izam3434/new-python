phonebook = {'Chaiwat': '777-1111', 'Palm': '777-2222', 'Kim': '777-3333'}

print(phonebook)

print(phonebook['Palm'])
print(phonebook.get('Kim'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' is not found in the phonebook.')

phonebook['Chaiwat'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Palm'] = '777-2122'
print(phonebook)

del phonebook['Kim']
print(phonebook)