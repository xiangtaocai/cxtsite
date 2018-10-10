class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
    def set_number_served(self,served):
        "Allow user to set the number of customers that have been served."
        self.number_served = served
       # print("The numbers of served customers are " + str(served))
        print("\nNumber served: " + str(restaurant.number_served))

    def increment_number_served(self,additional_served):
        """
        Allow user to increment the number of customers served.

        """
        self.number_served += additional_served
        print("\nNumber served: " + str(restaurant.number_served))


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
print("\nNumber served: " + str(restaurant.number_served))

restaurant.number_served = 430
print("\nNumber served: " + str(restaurant.number_served))

restaurant.set_number_served(1258)

restaurant.increment_number_served(253)





#ex.2
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
        """
        登录次数加一
        :return: ｉｎｔ
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        ":return to zero"
        self.login_attempts = 0
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
#eric.describe_user()
#eric.greet_user()
eric.increment_login_attempts()
print(eric.login_attempts)
eric.increment_login_attempts()
eric.increment_login_attempts()
print(eric.login_attempts)

eric.reset_login_attempts()
print(eric.login_attempts)


