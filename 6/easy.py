# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
# о том что машина поехала, остановилась, повернула(куда)
class Car:

    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        self.speed = self.speed * 0.8
        print('машина поехала')

    def stop(self):
        self.speed = 0
        print('машина остановилась')

    def turn(self, direction):
        self.direction = direction
        if self.speed != 0:
            if self.direction == 'вправо':
                print('машина повернула ' + self.direction)
            elif self.direction == 'влево':
                print('машина повернула ' + self.direction)
        else:
            print('машина остановлена и руль вывернут в сторону(ПДД)')

    # to appoint a policeman
    def make_police(self):
        self.is_police = True

    def show(self):
        if self.is_police:
            print('Машина: {} Цвета: {} Движется со скоростью: {}'.format(self.name, self.color, self.speed) + ' Полицейская ')
        else:
            print('Машина: {} Цвета: {} Движется со скоростью: {}'.format(self.name, self.color, self.speed))


if __name__ == '__main__':
    TownCar = Car(60, 'red', 'BoofCar')
    # Town
    TownCar.go()
    TownCar.show()
    TownCar.turn('влево')
    TownCar.stop()
    TownCar.show()
    TownCar.turn('вправо')
    # Sport
    SportCar = Car(370, 'white', 'Porshe')
    SportCar.go()
    SportCar.show()
    SportCar.turn('влево')
    SportCar.stop()
    SportCar.show()
    SportCar.turn('вправо')
    # Work
    WorkCar = Car(60, 'Orange', 'Kia')
    WorkCar.go()
    WorkCar.show()
    WorkCar.turn('влево')
    WorkCar.stop()
    WorkCar.show()
    WorkCar.turn('вправо')
    # Police
    PoliceCar = Car(220, 'Black', 'Ford')
    PoliceCar.make_police()
    PoliceCar.go()
    PoliceCar.show()
    PoliceCar.turn('влево')
    PoliceCar.stop()
    PoliceCar.show()
    PoliceCar.turn('вправо')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

# Супер машина имеющая возможность скорости * уровень_преводсходства
print('\n')
class SuperCar(Car):
     def __init__(self, speed, color, name, level_of_superiority):
         super().__init__(speed, color, name)
         self.level_of_superiority = level_of_superiority
         self.speed = self.speed * level_of_superiority


TownCarSuper = SuperCar(60, 'red', 'BoofCarSuper', 2)
TownCarSuper.go()
TownCarSuper.turn('влево')
TownCarSuper.show()
TownCarSuper.stop()
TownCarSuper.show()
TownCarSuper.turn('влево')
