# Базовий клас, який представляє транспортний засіб
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make          # Public
        self.model = model        # Public
        self._year = year         # Protected
        self.__mileage = 0        # Private

    def drive(self, miles):
        self.__add_mileage(miles)
        print(f"Driving {miles} miles. Total mileage: {self.__mileage} miles.")

    def get_year(self):
        return self._year

    def __add_mileage(self, miles):
        if miles > 0:
            self.__mileage += miles

    def get_mileage(self):
        return self.__mileage


# Клас Car, який наслідує Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  # Public

    def refuel(self):
        print(f"Refueling the {self.fuel_type} car.")

    def drive(self, miles):
        if self.fuel_type != "electric":
            super().drive(miles)
        else:
            print("This car cannot be refueled with conventional fuel.")


# Клас ElectricCar, який наслідує Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year, fuel_type="electric")
        self.__battery_capacity = battery_capacity  # Private

    def charge(self):
        print(f"Charging the car to {self.__battery_capacity} kWh.")

    def drive(self, miles):
        print(f"Driving electric car {miles} miles.")
        super().drive(miles)


# Використання класів
vehicle = Vehicle("Generic", "Model", 2020)
car = Car("Toyota", "Camry", 2021, "gasoline")
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

vehicle.drive(50)
car.refuel()
car.drive(100)
electric_car.charge()
electric_car.drive(150)

# Перевірка інкапсуляції
print(vehicle.get_year())         # Доступ до protected атрибуту
print(vehicle.get_mileage())      # Доступ до private атрибуту через публічний метод
