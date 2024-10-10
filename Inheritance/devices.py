class Device:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        print(f"{self.brand} {self.model} is now powered on.")
    
    def turn_off(self):
        print(f"{self.brand} {self.model} is now powered off.")

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"
    
class Laptop(Device):
    def __init__(self, ram: int, brand: str, model: str, price: float):
        super().__init__(brand, model, price)
        self.ram = ram

    def open_laptop(self):
        print(f"{self.brand} {self.model} is now opened.")

    def __str__(self) -> str:
        info = super().__str__()
        return f"{info}, Ram Size: {self.ram} GB"
    
class Smartphone(Device):
    def __init__(self, camera_resolution: int, brand: str, model: str, price: float):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo with a {self.camera_resolution} MP camera.")
    
    def __str__(self) -> str:
        info = super().__str__()
        return f"{info}, Camera Resolution: {self.camera_resolution} MP"
    
if __name__ == "__main__":
    phone1 = Smartphone(200, "Apple", "iphone15", 999.99, )
    phone1.turn_on()
    phone1.take_photo()
    print(phone1)
    laptop1 = Laptop(32, "dell", "2020", 1200)
    laptop1.open_laptop()
    laptop1.turn_off()
    print(laptop1)
