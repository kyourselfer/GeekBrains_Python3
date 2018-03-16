# Задача-1:
# Напишите скрипт, удаляющий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
print(__name__)
if __name__ == '__main__':
    import os


def delete_dir(a1):
    os.rmdir(a1)

if __name__ == '__main__':
    [delete_dir('dir_{}'.format(i)) for i in range(1, 10)]