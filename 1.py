a = 2
b=3
c=a+b
print (c)

a = 2
b=3
print (a+b)

print ('Привет мир!')

c=a-b
print (c)

c=a*b
print (c)

c=a**b
print (c)

c=a/b
print (c)

a = 2.1
b=3.3
c=a+b
print (c)

a = 3.1
b=0.1
c=a-b
print (c)

a = 3.1
b=0.1
c=a<b
print (c)

a = 3.1
b=0.1
c=a>b
print (c)

a = 3.1
b=0.1
c=a!=b
print (c)

a = 3.1
b=0.1
c=a==b
print (c)

a = 'Привет'
b='мир'
c=a + ' ' + b + '!'
print (c)

a = 'Привет'
b='всем'
print (a + ' ' + b + '!')

a = 'Здравствуйте'
b='все'
c= 2
d='{} {} {}!' .format (a, b, c)
print (d)

user = 'Вася'
d='{}, {}!' .format (a, user)
print (d)

user = 'Петя'
d='Привет, {name}!' .format (name=user)
print (d)

user = 'Иван'
d = f'Добрый день, {user}!'
print (d)
print (len (d))

user = 'Николай' .upper ()
print (user)

user = 'Николай' .lower ()
print (user)

user = 'николай' .capitalize ()
print (user)

user ='   Александр'
print (user)
print (len (user))
user1 = user.strip ()
print (user1)
print (len (user1))

a= 'Палажить'
b= a.replace ('а', 'о')
print (a)
print (b)

a= 'ПАиграть'.lower() .replace ('а', 'о')  .capitalize ()
print (a)

a= 'ПАиграть'
b=a.lower() .replace ('а', 'о')  .capitalize ()
print (a)
print (b)

a='67,906,97643'
print (a.split(','))

a= 'Заходите к  нам на    огонек'
b=a.split()
print (b)
print (len (b))

a=None
b=0
print (a is None)
print (b is None)
print (b is not None)

a='2.0'
b= 2
c=2.0
print (type (a))
print (type (b))
print (type (c))

name=input ('Введите Ваше имя: ')
print (f'Привет, {name}!')

age= int (input ('Сколько Вам лет? '))
birth_year=2019-age
print (f'Вы родились в {birth_year} году')

print (bool ('Ну, погоди!')) #Не пустая строка, не ноль и не None - True
print (bool (''))
print (bool  (111))
print (bool (0))
print (bool  (0.001))
print (bool (None))
print (bool (-2))

