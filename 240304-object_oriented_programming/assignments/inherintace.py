# Class ini berfungsi sebagai blueprint untuk
# membuat objek vehicle yang mempunyai
# atribut name, color, year_production, capacity, dan mileage dan method set_capacity
class Vehicle:
    # Konstruktor ini menginisialisasi variabel instance
    # name, color, year_production, capacity, dan mileage dengan nilai argumen
    def __init__(self, name, color, year_production, capacity, mileage):
        self.name = name
        self.color = color
        self.year_production = year_production
        self.capacity = capacity
        self.mileage = mileage
    # Mendefinisikan method bernama set_capacity yang
    # memiliki argumen self, capacity yang digunakan untuk
    # mengubah nilai capacity
    def set_capacity(self, capacity):
        self.capacity = capacity
# Class ini berfungsi sebagai blueprint untuk objek truck yang merupakan
# inherited class dari vehicle sehingga memiliki atribut dan method yang di turunkan
class Truck(Vehicle):
    pass
# instansiasi objek truck yang merupakan inherited class dari vehicle
truck = Truck(name="Tesla Truck", color="Gray", year_production=2024, capacity=9000, mileage=50)
print("Name:", truck.name)
print("Color:", truck.color)
print("Year of Production:", truck.year_production)
print("Capacity:", truck.capacity)
print("Mileage:", truck.mileage)
truck.set_capacity(10000)
print("Updated Capacity:", truck.capacity)
print("\nProgram Completed!\n\n--- By L200220277 ---")