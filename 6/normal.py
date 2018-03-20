# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor

# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инк

class Person:
    '''Родитель персоны'''

    def __init__(self):
        # attributes
        self.name = ''
        self.health = 100
        self.damage = 10
        self.armor = 20

    # methods
    ###########
    def _show_attr(self):
        return 'Здоровье: {} Урон: {} Защита: {} '.format(self.health, self.damage, self.armor)


class Player(Person):
    def __init__(self):
        super().__init__()

    def set_name(self, create_name):
        self.name = create_name
        print('Присвоино имя: ', self.name)

    def get_name(self):
        return self.name

    def show(self):
        print('Имя игрока: {}, {}'.format(self.get_name(), self._show_attr()))


class Enemy(Person):
    def __init__(self):
        super().__init__()

    def set_name(self, create_name):
        self.name = create_name
        print('Присвоино имя: ', self.name)

    def get_name(self):
        return self.name

    def show(self):
        print('Имя чужого: {}, {}'.format(self.get_name(), self._show_attr()))


Player1 = Player()
Player1.set_name('Kolya')
Player1.show()

# Enemy.
Enemy1 = Player()
Enemy1.set_name('Buriy')

com = """def generate_person(name, health=100, damage=50):
    return {'name': name, 'health': health, 'damage': damage}


def attack(who_attack, who_defend):
    who_defend['health'] -= who_attack['damage'] 


def pow(x, y):
    return 100


if __name__ == '__main__':
    print('РЎРІРѕР№ РєРѕРґ, РєРѕС‚РѕСЂС‹Р№ РЅРµ РґРѕР»Р¶РµРЅ РІС‹РїРѕР»РЅСЏС‚СЊСЃСЏ РїСЂРё РёРјРїРѕСЂС‚Рµ!')
    print(__name__)"""
