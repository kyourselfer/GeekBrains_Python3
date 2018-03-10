# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# 1
print('\n\t\t\t--- Task #1 ---:\n')
l1 = [i for i in range(1, 10, 2)]
l1n = l1.copy()
l1n = [i ** 2 for i in l1n]
print(l1, '\ti ** 2 =\t', l1n)


# 2
print('\n\t\t\t--- Task #2 ---:\n')
fruitsBox1 = ['passion fruit', 'water melon', 'pear', 'melon', 'kiwi']
fruitsBox2 = ['pear', 'plum', 'passion fruit']

fruitsBoxEq = [x for x in fruitsBox1 if x in fruitsBox2]
print('Equal fruits from Box 1 and Box 2: ', fruitsBoxEq)

# 3
print('\n\t\t\t--- Task #3 ---:\n')
import random

count = 0
while True:
    # Генерируем произвольное кол-во элем. с случ. числом
    ran_gen = [j for j in range(-100, 100, random.randrange(1, 100))]
    # Выбираем элем. из списка удовлетворяющие условиям ...
    ran_num = [i for i in ran_gen if (i % 3) == 0 and i == abs(i) and (i % 4) != 0]
    if ran_num == []:
        count += 1
        ran_gen = [j for j in range(-100, 100, random.randrange(1, 100))]
    else:
        print('Мы имеем список:\n{}\n'
              'Елемент(ы) удовлетворяющие условию'
              ' \"положительный и кратный 3 и не кратный 4\" найден(ы):\n'
              '\t{}'.format(ran_gen, ran_num))
        break
if count > 1:
    print(2 * '\n\t', 'Кол-во попыток =', count, '\n')

