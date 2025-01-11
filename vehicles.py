class Vehicle:
        vehicle_count=0

        def __init__(self,make:int,model:str):
                    self.make=make
                    self.model=model
                    self.increment_vehicle_count()
        def increment_vehicle_count(self):
                    Vehicle.vehicle_count+=1

        def get_vehicle_count(self):
                    return self.vehicle_count

        def start_engine(self):
                    print('Vehicle Engine Started')

        def __repr__(self):
                return f'this is a vehicle of a model {self.model} built in {self.make}'

class Car(Vehicle):
        def __init__(self,make,model,number_of_wheels=4):
                super().__init__(make,model)
                self.number_of_wheels=number_of_wheels

        def start_engine(self):
                print('Car Engine Started')
                super().start_engine()

class ElectricVehicle(Vehicle):
        def __init__(self,make,model,battery_capacity):
                super().__init__(make,model)
                self.battery_capacity=battery_capacity



class ElectricCar(Car,ElectricVehicle):
        def __init__(self,make,model,navigation_system):
                super().__init__(make,model)
                self.navigation_system=navigation_system

        def AutoDrive(self):
                print('Electric car is driving automatically')

        def start_engine(self):
                print('Electric car engine started')
                super().start_engine()


Car1=Car(1892,'bmw')
Car2=Car(1998,'mercedes')
Car3=ElectricCar(1994,'tesla','new navigation system')

print(Car1)
print(Car2)

print(Car3.get_vehicle_count())
