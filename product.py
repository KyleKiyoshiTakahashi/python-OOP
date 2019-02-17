# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. 
# If the item is being returned because it is defective, change status to "defective" and change price to 0. 
# If it is being returned in the box, like new, mark it "for sale". 
# If the box has been opened, set the status to "used" and apply a 20% discount.  
# (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
    def __init__(self, price, item_name, weight, brand, tax):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax = tax

    def Sell(self):
        print(str(self.item_name), "has been sold")
        self.status = "sold"
        return self

    def Add_tax(self, tax):
        print(str(self.tax), "is the tax")
        self.price = self.price + tax
        return self

    def Return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason_for_return == "opened box":
            self.status = "used"
            self.price *= .80

    def Display_info(self):
        print("Price: $"+ str(self.price))
        print("Item:", str(self.item_name))
        print("Weight:", str(self.weight))
        print("Brand:", str(self.brand))
        print("Status:", str(self.status))
        print("     ")

product1 = Product(15, "Cake", "4 lbs", "BestBakery", "1.20")
product1.Sell()
product1.Display_info()
product1.Return_item("opened box")
product1.Display_info()
product1.Add_tax(1.20)
product1.Display_info()







