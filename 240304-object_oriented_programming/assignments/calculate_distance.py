# Class ini digunakan untuk memberikan nilai x dan y untuk menentukan titik koordinat
# kemudian dapat menemukan jarak anatar titik koordinatnya
class CalculateDistance:
    # Konstruktor ini menginisialisasi variabel instance x dan y dengan nilai argumen
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Mendefinisikan method bernama set_location yang mengambil tiga argumen yaitu self, x, dan y.
    # kemudian variabel x dan y di set dari nilai x dan y dari argumen
    def set_location(self, x, y):
        self.x = x
        self.y = y
    # Mendefinisikan method bernama distance_from_origin yang digunakan untuk
    # Menghitung jarak titik dari titik asal menggunakan rumus jarak Euclidean.
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    # Mendefinisikan method bernama distance yang digunakan untuk
    # menghitung jarak antara 2 titik menggunakan rumus jarak Euclidean.
    def distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
coordinate_point_1 = CalculateDistance(0, 0)
print(f"Distance from origin for coordinate_point_1(at ({coordinate_point_1.x}, {coordinate_point_1.y})):", coordinate_point_1.distance_from_origin())
coordinate_point_1.set_location(3, 4)
coordinate_point_2 = CalculateDistance(8, 10)
print(f"Distance from origin for coordinate_point_1(at ({coordinate_point_1.x}, {coordinate_point_1.y})):", coordinate_point_1.distance_from_origin())
print("Distance from origin for coordinate_point_2:", coordinate_point_2.distance_from_origin())
print("Distance between point1 and point2:", coordinate_point_1.distance(coordinate_point_2))
print("\nProgram Completed!\n\n--- By L200220277 ---")