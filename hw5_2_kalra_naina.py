# hw5_2_kalra_naina.py
# CS1350 OOP Module - Homework Assignment 2
#Polymorphism, Advanced Methods, and Operator Overloading


#starter code-
from abc import ABC, abstractmethod
import math

# -------- Problem 1: Shapes --------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        print(f"{name} must be positive!")
        return False

class Circle(Shape):
    def __init__(self, radius):
        if not Shape.validate_positive(radius, "radius"):
            raise ValueError("Invalid radius")
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if not Shape.validate_positive(width, "width"):
            raise ValueError("Invalid width")
        if not Shape.validate_positive(height, "height"):
            raise ValueError("Invalid height")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not Shape.validate_positive(side1, "side1"):
            raise ValueError("Invalid side1")
        if not Shape.validate_positive(side2, "side2"):
            raise ValueError("Invalid side2")
        if not Shape.validate_positive(side3, "side3"):
            raise ValueError("Invalid side3")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(s.area() for s in self.shapes)

    def total_perimeter(self):
        return sum(s.perimeter() for s in self.shapes)


# -------- Problem 2: Pizza system (factory methods, static utilities) --------
class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not Pizza.validate_size(size):
            raise ValueError("Invalid size")
        self.size = size.lower()
        self.toppings = list(toppings)

    def calculate_price(self):
        base = Pizza.price_list[self.size]
        return base + Pizza.topping_price * len(self.toppings)

    def __str__(self):
        # lowercase size and wording to match expected output
        return f"{self.size} pizza with {len(self.toppings)} toppings - ${self.calculate_price()}"

    @classmethod
    def create_margherita(cls, size):
        return cls(size.lower(), ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size.lower(), ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size.lower(), ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size and size.lower() in ['small', 'medium', 'large']


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_number = PizzaOrder.total_orders
        self.order_id = f"ORDER_{self.order_number:03d}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(p.calculate_price() for p in self.pizzas)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"


class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        order = PizzaOrder()
        items = [it.strip() for it in order_string.split(',') if it.strip()]
        for item in items:
            parts = item.split()
            if len(parts) >= 2:
                size = parts[0].lower()
                ptype = parts[1].lower()
                if ptype == 'pepperoni':
                    pizza = Pizza.create_pepperoni(size)
                elif ptype == 'margherita':
                    pizza = Pizza.create_margherita(size)
                elif ptype == 'veggie':
                    pizza = Pizza.create_veggie(size)
                else:
                    # fallback: basic pizza without toppings (not expected in tests)
                    pizza = Pizza(size, [])
                order.add_pizza(pizza)
        return order

    @staticmethod
    def format_receipt(order):
        lines = []
        lines.append("=== RECEIPT ===")
        lines.append(f"Order: {order.order_id}")
        lines.append("Items:")
        for p in order.pizzas:
            lines.append(f"{p}")
        lines.append(f"Total: ${order.get_total()}")
        lines.append("==============")
        return "\n".join(lines)


# -------- Problem 3: Duration class with operator overloading --------
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Negative values not allowed")
        # Normalize overflow: seconds -> minutes, minutes -> hours
        extra_min, seconds = divmod(seconds, 60)
        minutes += extra_min
        extra_hours, minutes = divmod(minutes, 60)
        hours += extra_hours
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours:
            parts.append(f"{self.hours}h")
        if self.minutes:
            parts.append(f"{self.minutes}m")
        if self.seconds:
            parts.append(f"{self.seconds}s")
        if not parts:
            return "0s"
        return " ".join(parts)

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total = self.total_seconds + other.total_seconds
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return Duration(h, m, s)

    def __sub__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total = self.total_seconds - other.total_seconds
        if total <= 0:
            return Duration(0,0,0)
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return Duration(h, m, s)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise TypeError("Multiplier must be an integer")
        if multiplier < 0:
            raise ValueError("Multiplier must be non-negative")
        total = self.total_seconds * multiplier
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return Duration(h, m, s)

    def __eq__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.total_seconds <= other.total_seconds


# -------- Testing (same tests as in starter) --------
if __name__ == "__main__":
    # Problem 1
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f"{shape.describe()}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")

    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f"Total Area: {collection.total_area():.2f}")
    print(f"Total Perimeter: {collection.total_perimeter():.2f}")

    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        # validate_positive will already print "radius must be positive!"
        print("Correctly rejected negative radius")

    # Problem 2
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")
    print("\nIndividual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
        print(f"{pizza} - ${pizza.calculate_price()}")

    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")

    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string("large pepperoni, small margherita, medium veggie")
    print(OrderManager.format_receipt(order2))
    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")

    # Problem 3
    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)
    print("\nDurations:")
    print(f"d1 = {d1}")
    print(f"d2 = {d2}")
    print(f"d3 = {d3}")

    print("\nArithmetic:")
    print(f"d1 + d2 = {d1 + d2}")
    print(f"d3 - d1 = {d3 - d1}")
    print(f"d2 * 3 = {d2 * 3}")

    print("\nComparisons:")
    print(f"d1 == d2? {d1 == d2}")
    print(f"d1 < d3? {d1 < d3}")
    print(f"d2 <= d1? {d2 <= d1}")

    durations = [d3, d1, d2]
    durations.sort()
    print("\nSorted durations:")
    for d in durations:
        print(d)

    print("\nOverflow test:")
    d4 = Duration(0, 90, 90)  # -> 1h 31m 30s
    print(f"Duration(0, 90, 90) = {d4}")

    print(f"\nRepr: {repr(d1)}")
