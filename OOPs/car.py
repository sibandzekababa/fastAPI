class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color  

    def description(self):
        return f'{self.color} {self.brand} {self.model}'

    def drive(self):
       
        return f'{self.description()} is driving.'

    def turn(self):
       
        return f'{self.description()} is turning.'

  # ... your existing class code up to line 16 ...

# --- Add these lines starting at line 18 ---
my_car = Car(brand="Toyota", model="Prado", color="Black")
print(my_car.drive())
print(my_car.turn())
  



class ElectricalCar(Car):
    def __init__(self, brand, model, color, battery_life="10 kilometers"):
        super().__init__(brand, model, color)
        self.battery_life = battery_life 

    def charge(self):
        return f'{self.description()} is charging. Battery life: {self.battery_life}.'


if __name__ == "__main__":
    my_car = Car(brand="Toyota", model="Prado", color="Black")
    print(my_car.drive())

    my_ev = ElectricalCar(brand="Tesla", model="Model 3", color="White", battery_life="500 kilometers")
    print(my_ev.drive())   
    print(my_ev.charge()) 