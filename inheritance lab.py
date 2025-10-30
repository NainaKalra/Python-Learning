# # Beginner Level
# # TODO: Create Vehicle base class and Car derived class

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.brand} {self.model} is starting")

# # TODO: Create Car class that inherits from Vehicle
# class Car(Vehicle):
#     def honk(self):
#         # Print "Beep beep!"
#         print("Beep beep!")

# # Test:
# my_car = Car("Toyota", "Camry")
# my_car.start() 
# my_car.honk()   

# Intermediate Level (without using super())

# class Vehicle:
#     def __init__(self, brand, model, wheels):
#         self.brand = brand
#         self.model = model
#         self.wheels = wheels

#     def start(self):
#         print(f"{self.brand} {self.model} is starting")

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         # Cars have 4 wheels
#         Vehicle.__init__(self, brand, model, 4)
        
# class Motorcycle(Vehicle):
#     def __init__(self, brand, model):
#         # Motorcycles have 2 wheels
#         Vehicle.__init__(self, brand, model, 2)
        
#     def wheelie(self):
#             print(f"{self.brand} {self.model} does a wheelie!")
            
# car_name = Car("Mercedes", "Benz")
# bike_name = Motorcycle("Harley", "Davidson")

# car_name.start()
# bike_name.start()
# bike_name.wheelie()

# Beginner Level

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         return 0  # Base shape has no area

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__("Rectangle")  # Call parent constructor to set name
#         self.width = width
#         self.height = height

#     def area(self):
#         # Override to return width * height
#         return self.width * self.height

# # Test:
# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}")

# # Intermediate Level

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def calculate_grade(self):
#         # Regular grading
#         if self.score >= 90: return "A"
#         elif self.score >= 80: return "B"
#         elif self.score >= 70: return "C"
#         else: return "F"

# class HonorsStudent(Student):
#     def calculate_grade(self):
#         # Harder grading for honors
#         if self.score >= 95: return "A"
#         elif self.score >= 85: return "B"
#         elif self.score >= 75: return "C"
#         else: return "F"

# # Test both student types
# regular = Student("Alex", 88)
# honor = HonorsStudent("Alina",91)

# print(f"{regular.name}'s grade: {regular.calculate_grade()}")      # Honors
# print(f"{honor.name}'s grade: {honor.calculate_grade()}")      # Honors

# # Advanced Level

# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#         self.max_health = health

#     def attack(self):
#         return 10  # Base damage

#     def take_damage(self, amount):
#         self.health -= amount
#         print(f"{self.name} takes {amount} damage! Remaining health: {self.health}")

# class Warrior(Character):
#     def attack(self):
#         # Warriors do 2x damage
#         return 10 * 2

#     def take_damage(self, amount):
#         # Warriors have armor, reduce damage by 3 (minimum 0)
#         reduced = max(0, amount - 3)
#         self.health -= reduced
#         print(f"{self.name}'s armor reduces the damage by 3! It takes {reduced} damage. Health Left: {self.health}")

# class Mage(Character):
#     def __init__(self, name, health, mana):
#         # Initialize parent AND mana
#         Character.__init__(self, name, health)
#         self.mana = mana

#     def attack(self):
#         # If has mana, do 3x damage, else normal
#         if self.mana > 0:
#             self.mana -= 10  # Using some mana
#             return 10 * 3
#         else:
#             return 10

# # Test
# warrior = Warrior("Thor", 100)
# mage = Mage("Merlin", 80, 30)

# # Simulate attacks
# print(f"{warrior.name} attacks and deals {warrior.attack()} damage!")
# print(f"{mage.name} attacks and deals {mage.attack()} damage!")

# # Mage hits warrior
# warrior.take_damage(mage.attack())
# # Warrior hits mage
# mage.take_damage(warrior.attack())

# # Beginner Level

# class Student:
#     def __init__(self):
#         self.student_id = "S12345"
#         self.gpa = 3.5

#     def study(self):
#         print("Studying hard!")

# class Employee:
#     def __init__(self):
#         self.employee_id = "E67890"
#         self.salary = 20000

#     def work(self):
#         print("Working hard!")

# class StudentEmployee(Student, Employee):
#     def __init__(self, name):
#         # Initialize both parents
#         Student.__init__(self)
#         Employee.__init__(self)
#         # Add name attribute
#         self.name = name

# # Test:
# person = StudentEmployee("Alex")
# print(f"Name: {person.name}, Student ID: {person.student_id}, Employee ID: {person.employee_id}")
# person.study()
# person.work()

# Intermediate Level

class LandVehicle:
    def __init__(self):
        self.speed_on_land = 60

    def drive(self):
        print(f"Driving at {self.speed_on_land} mph")

class WaterVehicle:
    def __init__(self):
        self.speed_on_water = 30

    def sail(self):
        print(f"Sailing at {self.speed_on_water} knots")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, name):
        # Initialize both parent classes
        LandVehicle.__init__(self)
        WaterVehicle.__init__(self)
        self.name = name
        self.mode = "land" 
        
    def switch_mode(self):
        # Toggle between land and water
        if self.mode == "land":
            self.mode = "water"
            print(f"{self.name} switched to water mode.")
        else:
            self.mode = "land"
            print(f"{self.name} switched to land mode.")

# Test:
amphi = AmphibiousVehicle("AmphiX")
amphi.drive()          # Land mode
amphi.switch_mode()
amphi.sail()           # Water mode

# Advanced Level

class Camera:
    def __init__(self):
        self.megapixels = 12

    def capture(self):
        return "Photo taken!"

class Phone:
    def __init__(self):
        self.phone_number = "555-1234"

    def capture(self):  # Same method name!
        return "Screenshot taken!"

class SmartPhone(Phone, Camera):
    def __init__(self, model):
        # Initialize both parents
        Phone.__init__(self)
        Camera.__init__(self)
        self.model = model

    def capture(self, mode="phone"):
        # Let user choose which capture to use
        if mode == "phone":
            return Phone.capture(self)
        elif mode == "camera":
            return Camera.capture(self)
        else:
            return "Mode is not valid"

# Test:
smart = SmartPhone("Iphone 17 pro max")

print(smart.capture("camera"))
print(smart.capture("phone"))
