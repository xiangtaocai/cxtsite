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

class Battery():
    """专门描述电瓶的类"""
    def __init__(self,battery_size = 80):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，支出续航公里数"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        msg = "This car can go approximately " + str(range)
        msg += " miles on a full charge."
        print(msg)
class ElectricCar(Car):
    """
    special feature of electriccar

    """
    def __init__(self,make,model,year):
        """
        initial superclass

        :param make:
        :param model:
        :param year:
        """
        super().__init__(make,model,year)
        self.battery = Battery(70)


my_tesla = ElectricCar('tesla','models',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#例子１
class Restaurant():
    """
    A class presenting a restaurant
    """
    def __init__(self,restaurant_name,cuisine_type):
        "Initialize name and type"
        self.restaurant_name = restaurant_name.title()

        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        "Display a summary of the restaurant"
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)


    def open_restaurant(self):
        "Display a message chat the restaurant is open."
        msg = self.restaurant_name + " is open.Come on in."
        print("\n" + msg)


class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type = 'ice_cream'):
        super().__init__(restaurant_name,cuisine_type)
        #添加特有属性
        self.flavors = []


    def show_flavors(self):
        """display the flavors available"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(" - " + flavor.title())


big_one = IceCreamStand('The big one')
big_one.flavors = ['vanilla','chocolate','black cherry']


big_one.describe_restaurant()
big_one.show_flavors()


#例子２

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))


class Admin(User):

    def __init__(self,first_name,last_name,username,email,location):
        super().__init__(first_name,last_name,username,email,location)

        self.privileges = []


    def show_privileges(self):

        print("The following are privileges.")
        for privilege in self.privileges:
            print(" - " + privilege.title())

eric = Admin('tao','cai','taotai','326709@qq.com','beijing')
eric.privileges = ['can add post','can delete post','can ban user']

eric.describe_user()
eric.show_privileges()







class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Privileges():
    def __init__(self,privileges = []):

        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("The following are privileges.")
            for privilege in self.privileges:
                print(" - " + privilege.title())
        else:
            print("- This user has no privileges.")

class Admin(User):

    def __init__(self,first_name,last_name,username,email,location):
        super().__init__(first_name,last_name,username,email,location)

        self.privilege = Privileges()


eric = Admin('tao','cai','taotai','326709@qq.com','beijing')

eric.describe_user()
eric.privilege.show_privileges()
#先调用子类中的方法，在调用实例（单独类的实例）中的方法，溯源
eric.privilege.privileges = ['can add post','can delete post','can ban user']
eric.privilege.show_privileges()

#9-9

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("upgraded the battery to 85 kwh.")

        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model',2016)#battery是子类的属性，必须调用子类
my_tesla.get_descriptive_name()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

my_tesla.battery.upgrade_battery()




