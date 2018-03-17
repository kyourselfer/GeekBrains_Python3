# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
import os


def create_dir(a1):
    os.mkdir(a1)

if __name__ == '__main__':
    [create_dir('dir_{}'.format(i)) for i in range(1, 10)]

