# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print(2 * '\n' + 'Level: normal, Task:1\n')
import math

listr1 = [2, -5, 8, 9, -25, 25, 4]
listr1r = []
for i in listr1:
# если положительный элемент
    if i > 0:
# print('положительный элемент', i)
        j = math.sqrt(i)
# print('корень из ', i, '= ', j)
# если результат извлечения корня не имеет десятичной части
        if j == round(j):
# print('не имеет десятичной части: ', j)
            listr1r.append(round(j))
print('Дано: {}\nРезультат извлечения корней не имеющий десятичной части {}'.format(listr1, listr1r))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print(2 * '\n' + 'Level: normal, Task:2\n')
#
d1 = '05.03.2018'
print('Дата:', d1)
listd0 = {'01': 'первое', '02': 'второе', '03': 'третье',
          '04': 'четвертое', '05': 'пятое', '06': 'шестое',
          '07': 'седьмое', '08': 'восьмое', '09': 'девятое',
          '10': 'десятое', '11': 'одинадстое', '12': 'двенадцатое',
          '13': 'тринадцатое','14':'четырнадцотое', '15':'', '':'','':'','':'','':'','':''}
listd1 = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая',
          6: 'июня', 6: 'июля', 8: 'августа', 9: 'сентября',
          10: 'октября', 11: 'ноября', 12: 'декабря'}
d1g = d1.split('.')
dd = d1g[0]
mm = int(d1g[1])
yy = d1g[2]
print('Преобразованная дата: {:>8} {} {} года'.format(listd0[dd], listd1[mm], yy))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print(2 * '\n' + 'Level: normal, Task:3\n')
#
import random

n = random.randint(1, 20)
# listrand1 = random.sample(range(-100, 100), n)
listrand1 = [1, 2, 4, 5, 6, 2, 5, 2]
print('Список заполненный произвольными целыми числами: ', listrand1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print(2 * '\n' + 'Level: normal, Task:4\n')
# а)
listrandt = []
for z in listrand1:
    if z not in listrandt:
        listrandt.append(z)
print('Неповторяющиеся элементы исходного списка:', listrandt)

# б)
listrand2 = []
listrand3 = []

for x in listrand1:
    c1 = listrand1.count(x)
    listrand2.append(c1)
ci = 0
for y in listrand2:
    if y == 1:
        listrand3.append(listrand1[ci])
    ci = ci + 1
print('Элементы изходного списка которые не имеют повторений: ', listrand3, '\n')