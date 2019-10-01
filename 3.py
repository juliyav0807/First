capets={
    'name': 'Элегия',
    'size': '120x80',
    'color': 'Серый',
    'stock': 1
}
print (capets)

capets ['stock']=2

capets ['price']=7900

print (capets)

print (capets  ['name'])

print (capets.get('place', 'Москва')) # .get используем,чтобы не получить ошибку, 
# если запрашиваем несуществующий ключ. После ключа можно добавить, то значение, которое хотим, чтобы 
# выводилось для этого ключа. Если ничего не добавить будет выводиться None

del capets ['color']
print (capets)

