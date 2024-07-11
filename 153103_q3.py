# Fleet Management System

# Base Vehicle class with common attributes for all vehicles.
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

# Car class inheriting from Vehicle and adding a specific attribute for number of seats.
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

# Truck class inheriting from Vehicle and adding a specific attribute for cargo capacity.
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

# Motorcycle class inheriting from Vehicle and adding a specific attribute for engine capacity.
class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

# Fleet class to manage the fleet of vehicles.
class Fleet:
    def __init__(self):
        self.vehicles = []

    # Method to add a vehicle to the fleet.
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Method to display all vehicles in the fleet.
    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(f"Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")

    # Method to search for a vehicle by registration number.
    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")
                return
        print("Vehicle not found.")

def main():
    fleet = Fleet()
    while True:
        print("\nTransport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            reg_number = input("Enter vehicle registration number: ")
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            v_type = input("Enter vehicle type (car/truck/motorcycle): ").lower()
            if v_type == 'car':
                seats = int(input("Enter number of seats: "))
                vehicle = Car(reg_number, make, model, seats)
            elif v_type == 'truck':
                capacity = float(input("Enter cargo capacity: "))
                vehicle = Truck(reg_number, make, model, capacity)
            elif v_type == 'motorcycle':
                engine_capacity = float(input("Enter engine capacity: "))
                vehicle = Motorcycle(reg_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type.")
                continue
            fleet.add_vehicle(vehicle)
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            reg_number = input("Enter the registration number: ")
            fleet.search_vehicle(reg_number)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
