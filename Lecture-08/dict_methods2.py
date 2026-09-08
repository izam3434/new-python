phonebook = {'Chaiwat': '777-1111', 'Palm': '777-2222', 'Kim': '777-3333', 'Pluto': '777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Ironman'] = '888-2222'
print(heroesdict.get('Halk', 'Not found'))
print(heroesdict.get('Hulk', 'Not found'))

for key, value in heroesdict.items():
    print(key, value)

print(heroesdict.keys())
print(heroesdict.values())

print(heroesdict.pop('Mick', 'Not found'))
print(heroesdict.pop('Palm', 'Not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)