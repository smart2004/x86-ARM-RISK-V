# примеры кода на Python, демонстрирующие объект, класс, метод и атрибут в различных контекстах:

# Пример 1: Простой класс “Собака”

# 1. Класс
class Dog:
    # 2. Атрибуты класса (общие для всех собак)
    species = "Canis familiaris"

    # 3. Конструктор (метод для создания объекта)
    def __init__(self, name, breed, age):
        # 4. Атрибуты объекта (уникальные для каждой собаки)
        self.name = name
        self.breed = breed
        self.age = age

    # 5. Методы объекта
    def bark(self):
        print("Woof!")

    def describe(self):
        print(f"Имя: {self.name}, Порода: {self.breed}, Возраст: {self.age}")

# 6. Создание объектов (экземпляров класса)
dog1 = Dog("Барт", "Лабрадор", 3)
dog2 = Dog("Белла", "Бульдог", 5)

# 7. Использование методов и атрибутов объектов
dog1.bark()  # Вызов метода bark() для dog1
dog2.describe() # Вызов метода describe() для dog2
print(f"Вид: {dog1.species}") # Доступ к атрибуту класса через объект (сработает и через Dog.species)
print(f"Возраст: {dog1.age}")  # Доступ к атрибуту объекта dog1

# Разбор:

# Класс (class Dog): Это чертеж или шаблон для создания объектов. 
# Он определяет общую структуру и поведение для всех собак.
# Атрибуты класса (species = "Canis familiaris"): Это характеристики, 
# которые являются общими для всех объектов этого класса. 
# В данном случае, все собаки принадлежат к одному виду.
# Метод (__init__): Это особый метод, который называется конструктором. 
# Он вызывается при создании объекта и инициализирует его атрибуты.
# Атрибуты объекта (self.name, self.breed, self.age): Это характеристики, 
# которые являются уникальными для каждого объекта. Каждая собака имеет свои имя, породу и возраст.
# Методы объекта (bark, describe): Это действия, которые может выполнять объект. 
# Они определяют поведение объекта.
# Объекты (dog1, dog2): Это конкретные экземпляры класса. 
# Каждая собака (dog1 и dog2) является отдельным объектом, созданным на основе класса Dog.


#Пример 2: Более абстрактный класс “Фигура”

import math

# 1. Класс
class Shape:
    # 2. Атрибут класса (пример использования)
    area_unit = "кв. ед."

    # 3. Конструктор (не обязательно в абстрактных классах)
    def __init__(self):
        pass

    # 4. Методы класса
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть переопределен в подклассах")
    
    def __str__(self):
        return "Объект класса Shape"

# 5. Подкласс "Круг" (унаследован от Shape)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        # 6. Атрибут объекта
        self.radius = radius

    # 7. Переопределение метода calculate_area для круга
    def calculate_area(self):
        return math.pi * self.radius**2

    # 8. Переопределение метода __str__
    def __str__(self):
        return f"Объект класса Circle с радиусом {self.radius}"

# 9. Подкласс "Квадрат" (унаследован от Shape)
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        # 10. Атрибут объекта
        self.side = side

    # 11. Переопределение метода calculate_area для квадрата
    def calculate_area(self):
        return self.side**2

    # 12. Переопределение метода __str__
    def __str__(self):
        return f"Объект класса Square со стороной {self.side}"


# 13. Создание объектов (экземпляров классов)
circle = Circle(5)
square = Square(4)

# 14. Использование методов и атрибутов объектов
print(circle)
print(f"Площадь круга: {circle.calculate_area():.2f} {Shape.area_unit}")
print(square)
print(f"Площадь квадрата: {square.calculate_area():.2f} {Square.area_unit}")
print(f"Тип объекта square : {type(square)}")

# Разбор:

# Класс Shape: Это более абстрактный базовый класс. Он содержит общие методы для всех фигур, 
# но не реализует их, т.к. они зависят от конкретного типа.
# Атрибут класса area_unit: Это статическое значение для всех фигур.
# Метод __init__: Конструктор родительского класса, а в подклассах вызывается 
# super().init() для его выполнения.
# Метод calculate_area: Это абстрактный метод, который должен быть переопределен в подклассах.
# Класс Circle и Square: Это подклассы, унаследованные от класса Shape.
# Атрибуты объекта radius и side: Это характеристики, которые являются уникальными для 
# каждого круга и квадрата соответственно.
# Метод calculate_area в Circle и Square: Это переопределенные методы, 
# которые вычисляют площадь конкретной фигуры.
# Переопределенный метод __str__: Позволяет при печати объекта выводить о нем информацию.
# Объекты circle и square: Это конкретные экземпляры классов Circle и Square.
# Основные выводы:

# Класс – шаблон для создания объектов.
# Объект – конкретный экземпляр класса.
# Метод – функция, определенная внутри класса, которая может работать с данными объекта.
# Атрибут – переменная, связанная с классом или объектом, которая хранит информацию.
# Эти примеры иллюстрируют основные понятия объектно-ориентированного программирования в Python.