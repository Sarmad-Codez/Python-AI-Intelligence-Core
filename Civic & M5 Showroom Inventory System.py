# Vehicle Management System for GitHub Portfolio
class Car:
    def __init__(self, brand, model, year, plate_no):
        self.brand = brand
        self.model = model
        self.year = year
        self.plate_no = plate_no

    def display_details(self):
        print(f"[{self.brand.upper()}] Model: {self.model} | Year: {self.year} | Plate: {self.plate_no}")

class Showroom:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f" {car.brand} {car.model} added to inventory successfully!")

    def show_all_cars(self):
        if not self.inventory:
            print("Showroom is empty right now!")
            return
        print(f"\n--- Welcome to {self.name} ---")
        for car in self.inventory:
            car.display_details()

# Quick Testing
if __name__ == "__main__":
    my_showroom = Showroom("Sarmad's Luxury Motors")
    
    # Adding some heavy rides
    car1 = Car("Honda", "Civic RS", 2024, "SARMAD-01")
    car2 = Car("BMW", "M5 Competition", 2025, "SARMAD-05")
    
    my_showroom.add_car(car1)
    my_showroom.add_car(car2)
    
    my_showroom.show_all_cars()