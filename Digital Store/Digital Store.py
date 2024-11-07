class Phone:
    def __init__(self, id_, name, price, brand):
        self.id_ = id_
        self.name = name
        self.price = price
        self.brand = brand

    def display(self):
        print(f"Phone [ID: {self.id_}, Name: {self.name}, Price: {self.price}, Brand: {self.brand}]")

class Laptop:
    def __init__(self, id_, name, price, brand, memory, processor):
        self.id_ = id_
        self.name = name
        self.price = price
        self.brand = brand
        self.memory = memory
        self.processor = processor

    def display(self):
        print(f"Laptop [ID: {self.id_}, Name: {self.name}, Price: {self.price}, Brand: {self.brand}, Memory: {self.memory}, Processor: {self.processor}]")

class Store:
    def __init__(self):
        self.phones = {}
        self.laptops = {}

    def add(self, product):
        if isinstance(product, Phone):
            self.phones[product.id_] = product
            print("Added!")
        elif isinstance(product, Laptop):
            self.laptops[product.id_] = product
            print("Added!")

    def remove(self, r_id):
        if r_id in self.phones:
            del self.phones[r_id]
            print(f"Phone with ID : {r_id} removed")
        elif r_id in self.laptops:
            del self.laptops[r_id]
            print(f"Laptop with ID: {r_id} removed")
        else:
            print(f"ID: {r_id} doesnt exist")

    def display(self, type):
        type = type.lower()
        if type == "phone":
            for phone in self.phones.values():
                phone.display()
        elif type == "laptop":
            for laptop in self.laptops.values():
                laptop.display()


store = Store()

phone1 = Phone("P1", "IPhone 13", 699.99, "Apple")
laptop1 = Laptop("L1", "Rog", 999.99, "Asus", "32GB", "M1")
phone2 = Phone("P2", "Iphone 15", 999.99, "Apple")
laptop2 = Laptop("L2", "MacBook", 1899.99, "Apple", "64GB", "M1")

store.add(phone1)
store.add(laptop1)
store.add(phone2)
store.add(laptop2)

store.display("phone")
store.display("laptop")

store.remove("P1")
store.remove("P5")
store.remove("L2")
store.remove("L.3")

store.display("pHone")
store.display("laptop")