# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# 1
def whoami(n,a,c):
    print('{} {} год(а) проживает в городе {}'.format(n,a,c))


# 2
def maxnum(n1, n2, n3):
    return max(n1, n2, n3)


# 3
def strmax(*args):
    return max(*args)


print(2 * '\n' + 'Level: easy, Task:1\n')
nac = ['Vladimir', 32, 'Kislovodsk']
whoami(n,a,c)

print(2 * '\n' + 'Level: easy, Task:2\n')
print(maxnum(7, 5, 7))

print(2 * '\n' + 'Level: easy, Task:3\n')
str1 = 'General Public License'
str2 = 'Berkeley Software Distribution'
str3 = 'Gentoo Not Unix'
str4 = 'snjsm'

xl = list(map(lambda x: len(x), [str1, str2, str3, str4]))
print(strmax(*xl))
