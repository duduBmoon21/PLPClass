class Smartphone:
    """A class representing a smartphone"""
    
    def __init__(self, brand, model, storage, battery_level=100):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_level = battery_level
        self.is_on = False
    
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now powered on!"
        return "Phone is already on."
    
    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} is now powered off."
        return "Phone is already off."
    
    def check_battery(self):
        return f"Battery level: {self.battery_level}%"
    
    def use_phone(self, minutes):
        if self.is_on:
            battery_drain = minutes * 0.5
            self.battery_level = max(0, self.battery_level - battery_drain)
            return f"Used phone for {minutes} minutes. {self.check_battery()}"
        return "Cannot use phone while it's off."
    
    def charge(self, minutes):
        charge_amount = minutes * 1
        self.battery_level = min(100, self.battery_level + charge_amount)
        return f"Charged for {minutes} minutes. {self.check_battery()}"

class GamingPhone(Smartphone):
    """A specialized smartphone for gaming with enhanced features"""
    
    def __init__(self, brand, model, storage, ram, gpu, battery_level=100):
        super().__init__(brand, model, storage, battery_level)
        self.ram = ram
        self.gpu = gpu
        self.is_gaming_mode = False
    
    def activate_gaming_mode(self):
        if not self.is_gaming_mode:
            self.is_gaming_mode = True
            return "Gaming mode activated!"
        return "Gaming mode is already active."
    
    def deactivate_gaming_mode(self):
        if self.is_gaming_mode:
            self.is_gaming_mode = False
            return "Gaming mode deactivated."
        return "Gaming mode is not active."
    
    def use_phone(self, minutes):
        if self.is_on:
            drain_rate = 1.0 if self.is_gaming_mode else 0.7
            battery_drain = minutes * drain_rate
            self.battery_level = max(0, self.battery_level - battery_drain)
            mode = "gaming" if self.is_gaming_mode else "normal"
            return f"Used phone in {mode} mode for {minutes} minutes. {self.check_battery()}"
        return "Cannot use phone while it's off."

class SecurePhone(Smartphone):
    """A smartphone with enhanced security features"""
    
    def __init__(self, brand, model, storage, battery_level=100):
        super().__init__(brand, model, storage, battery_level)
        self.__pin_code = "0000"
    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin_code = new_pin
            return "PIN code updated successfully!"
        return "PIN must be 4 digits."
    
    def unlock(self, pin_attempt):
        if pin_attempt == self.__pin_code:
            return "Phone unlocked!"
        return "Incorrect PIN!"

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def move(self):
        return "The animal moves."
    
    def speak(self):
        return "The animal makes a sound."

class Bird(Animal):
    def move(self):
        return f"{self.name} the {self.species} is flying!"
    
    def speak(self):
        return "Chirp chirp!"

class Fish(Animal):
    def move(self):
        return f"{self.name} the {self.species} is swimming!"
    
    def speak(self):
        return "Blub blub!"

class Dog(Animal):
    def move(self):
        return f"{self.name} the {self.species} is running!"
    
    def speak(self):
        return "Woof woof!"

class Snake(Animal):
    def move(self):
        return f"{self.name} the {self.species} is slithering!"
    
    def speak(self):
        return "Hiss hiss!"

def demonstrate_polymorphism():
    """Show how different animals move and speak differently"""
    animals = [
        Bird("Sky", "Eagle"),
        Fish("Bubbles", "Goldfish"),
        Dog("Buddy", "Labrador"),
        Snake("Slither", "Python")
    ]
    
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 40)
    
    for animal in animals:
        print(f"{animal.move()}")
        print(f"{animal.speak()}")
        print("-" * 30)

if __name__ == "__main__":
    print("SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 40)
    
    my_phone = Smartphone("Apple", "iPhone 15", 256)
    print(my_phone.power_on())
    print(my_phone.use_phone(30))
    print(my_phone.charge(15))
    print(my_phone.power_off())
    
    print("\nGAMING PHONE DEMONSTRATION")
    gaming_phone = GamingPhone("ROG", "Phone 7", 512, 16, "Adreno 740")
    print(gaming_phone.power_on())
    print(gaming_phone.activate_gaming_mode())
    print(gaming_phone.use_phone(60))
    
    print("\nSECURE PHONE DEMONSTRATION")
    secure_phone = SecurePhone("Blackberry", "Classic", 128)
    print(secure_phone.set_pin("1234"))
    print(secure_phone.unlock("1234"))
    
    print("\n" + "=" * 40)
    demonstrate_polymorphism()