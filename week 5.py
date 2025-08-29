# Activity 1: Smartphone Classes

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.battery = battery  

    def show_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.model} charged. Battery now: {self.battery}mAh")


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)  
        self.cooling_system = cooling_system  
    def show_specs(self):
        super().show_specs()  
        print(f"Cooling System: {self.cooling_system}")


phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone1.show_specs()
phone1.charge(500)

gphone = GamingPhone("Asus", "ROG Phone 6", 256, 6000, "Advanced Liquid Cooling")
gphone.show_specs()



# Activity 2: Polymorphism with Animals


class Animal:
    def move(self):
        pass  


class Dog(Animal):
    def move(self):
        print("Dog is running")


class Bird(Animal):
    def move(self):
        print("Bird is flying ")


class Fish(Animal):
    def move(self):
        print("Fish is swimming ")


# Demonstrate polymorphism
animals = [Dog(), Bird(), Fish()]
for a in animals:
    a.move()
