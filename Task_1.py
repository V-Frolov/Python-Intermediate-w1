# Создать класс дробь(Fraction), конструктор которого принимает целые числа
# (num, den - числитель(numerator), знаменатель(denominator) ).
#
# Выполнить
#
# Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к
# атрибутам реализовать через свойства.
#
# Переопределить методы __sub__, __add__, __mull__, __truediv__
# для того, чтобы можно было выполнять соответствующие математические действия
# с объектами класса дробь.
# (Вычитание, сложение, умножение и деление).
#
# Добавить класс миксин, в котором реализовать статические методы, для этих же
# операций(add, sub, mull, div). Добавить класс миксин в класс Fraction
#
# Создать classmethod который из строки типа 'числитель/знаменатель' возвращает
# объект класса дробь.
#
# Переопределить метод __str__, который при выводе объекта на печать будет
# выводить строку вида num / den.
#
# Создать объекты класса дробь.
#
# Выполнить все реализованные методы.

class FractionMixin:
    @staticmethod
    def add(fr1, fr2):
        num = fr1.num * fr2.den + fr2.num * fr1.den
        den = fr1.den * fr2.den
        if den % num == 0:
            den = den // num
            num = 1
        return f'{num}/{den}'

    def sub(fr1, fr2):
        num = fr1.num * fr2.den - fr2.num * fr1.den
        den = fr1.den * fr2.den
        if den % num == 0:
            den = den // num
            num = 1
        return f'{num}/{den}'

    def mul(fr1, fr2):
        num = fr1.num * fr2.num
        den = fr1.den * fr2.den
        if den % num == 0:
            den = den // num
            num = 1
        return f'{num}/{den}'

    def div(fr1, fr2):
        num = fr1.num * fr2.den
        den = fr1.den * fr2.num
        if den % num == 0:
            den = den // num
            num = 1
        if num % den == 0:
            num = num // den
            den = 1
        return f'{num}/{den}'


class Fraction(FractionMixin):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        assert num != 0, "Numerator can't be equal 0"
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        assert den != 0, "Denominator can't be equal 0"
        self.__den = den

    def __add__(self, other):
        num = self.num * other.__den + other.__num * self.den
        den = self.den * other.__den
        if den % num == 0:
            den = den // num
            num = 1
        return self.__class__(num, den)

    def __sub__(self, other):
        num = self.num * other.__den - other.__num * self.den
        den = self.den * other.__den
        if den % num == 0:
            den = den // num
            num = 1
        return self.__class__(num, den)

    def __mul__(self, other):
        num = self.num * other.__num
        den = self.den * other.__den
        if den % num == 0:
            den = den // num
            num = 1
        return self.__class__(num, den)

    def __truediv__(self, other):
        num = self.num * other.__den
        den = self.den * other.__num
        if den % num == 0:
            den = den // num
            num = 1
        if num % den == 0:
            num = num // den
            den = 1
        return self.__class__(num, den)

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    @classmethod
    def from_string(cls, str_val):
        numden = [int(x) for x in str_val.split('/')]
        return Fraction(numden[0], numden[1])

fract1 = Fraction(1, 3)
fract2 = Fraction(1, 6)
fract = fract1 + fract2
print(f'{fract1} + {fract2} = {fract}')
fract = fract1 - fract2
print(f'{fract1} - {fract2} = {fract}')
fract = fract1 * fract2
print(f'{fract1} * {fract2} = {fract}')
fract = fract1 / fract2
print(f'{fract1} / {fract2} = {fract}')

fract3 = Fraction.add(fract1, fract2)
print(f'Mixin: {fract1} + {fract2} = {fract3}')
fract3 = Fraction.sub(fract1, fract2)
print(f'Mixin: {fract1} - {fract2} = {fract3}')
fract3 = Fraction.mul(fract1, fract2)
print(f'Mixin: {fract1} * {fract2} = {fract3}')
fract3 = Fraction.div(fract1, fract2)
print(f'Mixin: {fract1} / {fract2} = {fract3}')

fract4 = Fraction.from_string('4/5')
print(f'Classmethod from_string: {fract4}')

print(f'__str__: {fract1}')
