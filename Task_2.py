# Создать класс Point2D. Координаты точки задаются 2 параметрами - координатами
# x, y на плоскости.
# Реализовать метод distance который принимает экземпляр класса Point2D и
# рассчитывает расстояние между 2мя точками на плоскости.
# Создать защищенный атрибут класса - счетчик созданных экземпляров класса.
# Чтение количества экземпляров реализовать через метод getter.
#
# Создать класс Point3D, который является наследником класса Point2D.
# Координаты точки задаются 3 параметрами - координатами x, y, z в пространстве.
# Переопределить конструктор с помощью super().
# Переопределить метод distance для определения расстояния между 2-мя точками
# в пространстве.

class Point2D:
    __countOfExample = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__countOfExample += 1

    @classmethod
    @property
    def getCount(cls):
        return Point2D.__countOfExample

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f'{self.x}, {self.y}'


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2  + (self.z - point.z) ** 2) ** 0.5

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'


dot1 = Point2D(3, 2)
dot2 = Point2D(7, 5)
print(f'Distance between [{dot1}] and [{dot2}] = {dot1.distance(dot2)}')
print('Count of example:', Point2D.getCount)
dot3 = Point3D(3, 2, 8)
dot4 = Point3D(7, 5, 9)
print(f'Distance between [{dot3}] and [{dot4}] = {dot3.distance(dot4)}')
