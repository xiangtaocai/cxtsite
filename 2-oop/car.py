class Car():
    "模拟汽车的简单尝试"
    def __init__(self,make,model,year):
        "initialize car's attribute"
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        "Return descriptive information"
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        "打印车里程"
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi','a4',2018)
#第一个方法修改属性的值,再调用方法
my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
#第二个方法修改属性的值,定义一个方法，直接将值传递给一个方法内部更新。

#self.odometer_reading = mileage

#第三个方法,对属性的值进行递增


class Car():
    "模拟汽车的简单尝试"
    def __init__(self,make,model,year):
        "initialize car's attribute"
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        "Return descriptive information"
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        "打印车里程"
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        "更新到指定值"
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rool back the odometer.")
    def increment_odometer(self,miles):
        "增加指定量"
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't rool back the odometer.")



my_used_car = Car('subaru','outback',2000)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(25380)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()
