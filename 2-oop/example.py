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
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type +\
              "."
        print("\n" + msg)


    def open_restaurant(self):
        "Display a message chat the restaurant is open."
        msg = self.restaurant_name + " is open.Come on in."
        print("\n" + msg)

restaurant = Restaurant('the mean queen','pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#实例２
restaurant2 = Restaurant('yu jiameiwei','fishes')
restaurant2.describe_restaurant()
#实例3
restanrant3 = Restaurant('lao jin','shaokao')
restanrant3.describe_restaurant()

#创建user的类
class user():
    """
    A class discribe user and introduction
    """
    def __init__(self,first_name,last_name,city,position):
        "display where someone working and which position "
        self.first_name = first_name.title()
        self.last_name = last_name.lower()
        self.city = city.title()
        self.position = position

    def describe_user(self):
        "summerize about user"
        print("\n" + self.first_name + self.last_name + " come from " +
              self.city + " he(she) is a " + self.position + ".")

    def greet_user(self):
        "greeting"
        print("Hello " + self.first_name + self.last_name + " nice to meet you.")


user1 = user('eric','matthes','shanghai','saler')
user1.describe_user()
user1.greet_user()


