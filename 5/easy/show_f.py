# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(__name__)
import os

# print('\nВы находитесь в: {}\nСписок папок и файлов в текущей директории: {}'.format(os.getcwd(), os.listdir(path='.')))
def show(a1):
    return os.listdir(path=a1)

if __name__ == '__main__':
    print(show('.'))