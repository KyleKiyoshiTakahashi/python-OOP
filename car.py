# Assignment: Car
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# Create a class called  Car. In the __init__(), allow the user to specify the following 
# attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. 
# Otherwise, set the tax to be 12%.
# Create six different instances of the class Car. In the class have a method called display_all() 
# that returns all the information about the car as a string. In your __init__(), call this display_all() method 
# to display information about the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()


    def display_all(self):
        print('Price: $'+ str(self.price))
        print('Speed '+ str(self.speed))
        print('Fuel: '+ self.fuel)
        print('Mileage: '+ str(self.mileage))
        print('Tax: '+ str(self.tax))
        print("        ")

car1 = Car(20000, 35, 'Full', 150)
car2 = Car(3200, 155, 'Half Full', 200000)
car3 = Car(18000, 85, 'Empty', 12345)
car4 = Car(800, 35, 'Full', 5000)
car5 = Car(100000, 55, 'Empty', 15)
car6 = Car(37509, 165, 'Full', 5)


# A sample output would be like this:

# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

# Price: 2000
# Speed: 5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12

# Price: 2000
# Speed: 15mph
# Fuel: Kind of Full
# Mileage: 95mpg
# Tax: 0.12

# Price: 2000
# Speed: 25mph
# Fuel: Full
# Mileage: 25mpg
# Tax: 0.12

# Price: 2000
# Speed: 45mph
# Fuel: Empty
# Mileage: 25mpg
# Tax: 0.12

# Price: 20000000
# Speed: 35mph
# Fuel: Empty
# Mileage: 15mpg
# Tax: 0.15







