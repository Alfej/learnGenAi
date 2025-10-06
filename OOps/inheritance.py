class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.IsEngineOn = False
        self.speed = 0

    def start_engine(self):
        self.IsEngineOn = True
        return f"The engine of the {self.brand} {self.model} is starting."
    
    def stop_engine(self):
        self.IsEngineOn = False
        self.speed = 0
        return f"The engine of the {self.brand} {self.model} is stopping."
    
    def accelerate(self):
        if self.IsEngineOn:
            self.speed += 10
            return f"The {self.brand} {self.model} is accelerating. Current speed: {self.speed} km/h."
        else:
            return f"Start the engine first to accelerate the {self.brand} {self.model}."
        
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            return f"The {self.brand} {self.model} is braking. Current speed: {self.speed} km/h."
        else:
            return f"The {self.brand} {self.model} is already stationary."
    
class ManualCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.current_gear = 0

    def shift_gear(self, gear):
        if self.IsEngineOn:
            self.current_gear = gear
            return f"The {self.brand} {self.model} is shifting to gear {gear}."
        else:
            return f"Start the engine first to shift gears in the {self.brand} {self.model}."
        
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_level = 100  # percentage

    def charge_battery(self):
        self.battery_level = 100
        return f"The battery of the {self.brand} {self.model} is fully charged."
    
    def start_engine(self):
        if self.battery_level > 0:
            return super().start_engine()
        else:
            return f"The battery is empty. Please charge the {self.brand} {self.model} first."
        
if __name__ == "__main__":
    my_manual_car = ManualCar("Toyota", "Corolla")
    print(my_manual_car.start_engine())
    print(my_manual_car.shift_gear(1))
    print(my_manual_car.accelerate())
    print(my_manual_car.brake())
    print(my_manual_car.stop_engine())

    my_electric_car = ElectricCar("Tesla", "Model 3")
    print(my_electric_car.start_engine())
    print(my_electric_car.accelerate())
    print(my_electric_car.brake())
    print(my_electric_car.charge_battery())
    print(my_electric_car.stop_engine())
    