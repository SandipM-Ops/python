
class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        #self.total_car+=1
        #or 
        Car.total_car+=1
    def get_brand(self):
        return self.__brand + " !"  

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petorl or Diesel"
    
    def general_des(self):
        return "Cars are means transport"


class Electric_Car(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return "Charge"

mye_car = Electric_Car("Tesla", "Models", "85kwh")
print(mye_car.get_brand())
print(mye_car.fuel_type())
safari= Car("Tata","Safari")
print(safari.get_brand())
print(safari.fuel_type())

#print(Car.total_car)

print(mye_car.general_des())

class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        #self.total_car+=1
        #or 
        Car.total_car+=1
    def get_brand(self):
        return self.__brand + " !"  

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petorl or Diesel"
    
    def general_des(self):
        return "Cars are means transport"


class Electric_Car(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return "Charge"

mye_car = Electric_Car("Tesla", "Models", "85kwh")
print(mye_car.get_brand())
print(mye_car.fuel_type())
safari= Car("Tata","Safari")
print(safari.get_brand())
print(safari.fuel_type())

#print(Car.total_car)

class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        #self.total_car+=1
        #or 
        Car.total_car+=1
    def get_brand(self):
        return self.__brand + " !"  

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petorl or Diesel"
    @staticmethod
    def general_des():
        return "Cars are means transport"
    @property
    def model(self):
        return self.__model

class Electric_Car(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return "Charge"

mye_car = Electric_Car("Tesla", "Models", "85kwh")

print(isinstance(mye_car,Car))
print(isinstance(mye_car,Electric_Car))

#safaris= Car("Tata","Safari")
# safaris.model="City"
#print(safaris.model)
