class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
    def full_name(self):
        return f"{self.brand}{self.model}"
class Electric_Car(Car):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
mye_car= Electric_Car("Tesla", "Models","85kwh")
print(mye_car.full_name())