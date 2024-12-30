# SOLID – это аббревиатура, представляющая пять основных принципов объектно-ориентированного 
# программирования, которые помогают создавать более гибкий, поддерживаемый и масштабируемый код.

# 1. S – Single Responsibility Principle (Принцип единственной ответственности)

# Суть: Класс должен иметь только одну причину для изменения. Другими словами, 
# класс должен отвечать только за одну часть функционала.

# Плохой пример (нарушает SRP):

class OrderProcessor:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def save_order(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Items:{self.items}, Total:{self.calculate_total()}")

    def send_confirmation_email(self, email):
        print(f"Отправка подтверждения на {email}")
# Проблема: OrderProcessor отвечает за несколько вещей: расчет общей стоимости, 
# сохранение заказа и отправку письма. Это может привести к проблемам при внесении 
# изменений в одном из этих аспектов.

# Хороший пример (соблюдает SRP):

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

class OrderSaver:
    def save(self, order, filename):
        with open(filename, 'w') as f:
            f.write(f"Items:{order.items}, Total:{order.calculate_total()}")


class EmailSender:
    def send(self, email, message):
        print(f"Отправка сообщения на {email}: {message}")

# Использование:
order = Order([type('Item', (object,), {'price': 10, 'quantity': 2})(),
                type('Item', (object,), {'price': 5, 'quantity': 3})()])
order_saver = OrderSaver()
order_saver.save(order, 'order.txt')

email_sender = EmailSender()
email_sender.send("test@email.com", "Ваш заказ сформирован")

print(f"Общая сумма заказа: {order.calculate_total()}")
# Улучшение: Мы разделили функционал на отдельные классы Order (модель заказа), 
# OrderSaver (сохранение заказа) и EmailSender (отправка email). 
# Каждый класс теперь имеет только одну ответственность.

# 2. O – Open/Closed Principle (Принцип открытости/закрытости)

# Суть: Программные сущности (классы, модули, функции) должны быть открыты для расширения, 
# но закрыты для модификации.

# Плохой пример (нарушает OCP):

class Shape:
    def __init__(self, type, *args):
        self.type = type
        self.args = args
    
    def calculate_area(self):
        if self.type == "circle":
            radius = self.args[0]
            return 3.14 * radius ** 2
        elif self.type == "rectangle":
            width = self.args[0]
            height = self.args[1]
            return width * height
        #  При добавлении новой фигуры нужно будет изменять этот метод!
# Проблема: Когда мы захотим добавить новую фигуру (например, треугольник), 
# нам придется изменять класс Shape, что нарушает принцип OCP.

# Хороший пример (соблюдает OCP):

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape): # Добавление нового типа без модификации Shape
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

#Использование
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(f"Площадь: {shape.calculate_area()}")
# Улучшение: Мы ввели абстрактный базовый класс Shape и его подклассы Circle, Rectangle, Triangle. 
# Теперь мы можем добавлять новые фигуры, не изменяя существующий код, просто создавая новые 
# классы-наследники от Shape.

# 3. L – Liskov Substitution Principle (Принцип подстановки Барбары Лисков)

# Суть: Подклассы должны быть взаимозаменяемы со своими базовыми классами, не нарушая их корректность.

# Плохой пример (нарушает LSP):

class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Страус не летает!")
# Проблема: Ostrich не может “летать” и выбрасывает исключение, что делает его непригодным 
# для замены в коде, который ожидает Bird, что нарушает LSP.

# Хороший пример (соблюдает LSP):

from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass
    
class Duck(FlyingBird):
    def fly(self):
        print("Утка летает")
    def move(self):
        print("Утка плавает и летает")

class Ostrich(Bird):
    def move(self):
        print("Страус бегает")

def make_bird_move(bird):
    bird.move()

duck = Duck()
ostrich = Ostrich()
make_bird_move(duck) # OK
make_bird_move(ostrich) # OK
# Улучшение: Мы разделили поведение на move (общее для всех птиц) и 
# fly (только для летающих). Ostrich теперь не наследует метод fly, 
# который бы нарушал логику. Код теперь работает правильно.

# 4. I – Interface Segregation Principle (Принцип разделения интерфейса)

# Суть: Клиенты не должны зависеть от методов, которые они не используют. 
# Разбивайте большие интерфейсы на более мелкие и специфические.

# Плохой пример (нарушает ISP):

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def eat(self):
        pass

class Human(Worker):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")
class Robot(Worker):
    def work(self):
        print("Робот работает")

    def eat(self):
        raise Exception("Робот не ест!")
# Проблема: Robot не может есть, но вынужден реализовывать метод eat, что нарушает ISP.

# Хороший пример (соблюдает ISP):

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Worker, Eater):
    def work(self):
        print("Человек работает")
    def eat(self):
        print("Человек ест")

class Robot(Worker):
    def work(self):
        print("Робот работает")
# Улучшение: Мы разделили интерфейс на Worker и Eater. Теперь Robot реализует только Worker.

# 5. D – Dependency Inversion Principle (Принцип инверсии зависимостей)

# Суть:
# Высокоуровневые модули не должны зависеть от низкоуровневых. Оба должны зависеть от абстракций.
# Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
# Плохой пример (нарушает DIP):

class Keyboard:
    def press_key(self):
        print("Клавиша нажата")

class Monitor:
    def display(self, text):
        print(f"Отображено: {text}")

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
        self.monitor = Monitor()

    def start(self):
        self.keyboard.press_key()
        self.monitor.display("Компьютер включен")

computer = Computer()
computer.start()
# Проблема: Computer жестко зависит от конкретных реализаций Keyboard и Monitor. 
# Если мы захотим использовать другой тип клавиатуры или монитора, нам придется менять код в Computer.

# Хороший пример (соблюдает DIP):

from abc import ABC, abstractmethod

class InputDevice(ABC):
    @abstractmethod
    def press(self):
        pass
class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        pass

class Keyboard(InputDevice):
    def press(self):
        print("Клавиша нажата")

class Monitor(OutputDevice):
    def display(self, text):
        print(f"Отображено: {text}")

class Computer:
    def __init__(self, input_device:InputDevice, output_device:OutputDevice):
        self.input_device = input_device
        self.output_device = output_device

    def start(self):
        self.input_device.press()
        self.output_device.display("Компьютер включен")

#Использование
keyboard = Keyboard()
monitor = Monitor()

computer = Computer(keyboard, monitor)
computer.start()
# Улучшение: Computer теперь зависит от абстракций InputDevice и OutputDevice. 
# Мы можем передавать любые конкретные реализации этих интерфейсов.

# Заключение

# Применение принципов SOLID не является самоцелью, но они помогают создавать более гибкий, 
# поддерживаемый и масштабируемый код. Следование этим принципам может значительно улучшить 
# качество вашего программного обеспечения.
