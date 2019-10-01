hilos = ['Крестьянка', 'Ариадна', 'Хуторок', 'Пехорка', 'Снежинка']
print (hilos)
print (len (hilos))

hilos .append  ('Тюльпан') #Добавляет элемент в конец списка
print (len (hilos))

print (hilos.count ('Тюльпан')) #Считает количество указанных элементов в списке
print (hilos .count ('Ирис'))

print (hilos [0] )

print (hilos [0:5] ) #Взять все элементы с .. по ... (последний не включается)

print (hilos [-1]) #Напечает последний

print (hilos .index ('Тюльпан'))

hilos .sort ()
print (hilos)

print ('Травка' in hilos) # in проверяет есть ли этот элемент в этом списке

del hilos [3] # Удаляет элемент по индексу
print (hilos)

hilos .remove ('Пехорка') #Удаляет элемент по названию
print (hilos)
