class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"  # Corrected: __brand instead of ___brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

class Electric_Car(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

mye_car = Electric_Car("Tesla", "Models", "85kwh")
print(mye_car.get_brand())
# print(mye_car.__brand)