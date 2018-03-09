# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print(2 * '\n' + 'Level:easy, Task:1\n')
### Area of values
list1 = ['яблоко', 'банан', 'киви', 'арбуз']
### Body of code
for t in list1:
   # numbering
   n = list1.index(t)
   n = n + 1
   # alignment
   h = 6 - len(list1[n - 1])
   # output
   print(str(n) + '.{} '.format(h * ' ') + t)

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print(2 * '\n' + 'Level:easy, Task:2\n')
### Area of values
listr1 = ['ab', 12, 'cba', 777, 555, 777, 555, 'SHj']
listr2 = ['www', 777, 'hsjk', 12, 82928]
### Body of code
# compare listr1 and listr2
for i in listr1:
   for j in listr2:
       if i == j:
           # remove all matched values
           listr1.remove(j)
# output
print(listr1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print(2 * '\n' + 'Level:easy, Task:3\n')
### Area of values
listrd1 = [20, 65217, 3, 367, 6217, 200]
### Body of code
for k in listrd1:
   if k % 2 == 0:
       m = k // 4
       print(k, '// 4 = ', m)
   else:
       m = k * 2
       print(k, '* 2 = ', m)

