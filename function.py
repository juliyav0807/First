"""
Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, 
приводит их к строке и отдает объединенными через разделитель delimiter
Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
положите результат в переменную и выведите ее значение на экран
Сделайте так, чтобы результирующая строка выводилась заглавными буквами
"""

def get_summ (one, two, delimetr='&'):
   return f'{one} {delimetr} {two}' .upper()
        
g_s=get_summ ('Learn', 'python')
print (g_s)
