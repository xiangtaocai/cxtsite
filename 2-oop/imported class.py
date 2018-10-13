#导入类
from cars import Car

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#导入多个类
from cars import ElectricCar,Car

my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#导入一个模块
import cars
my_beetle =cars.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = cars.Car('tesla','roadster',2016)


