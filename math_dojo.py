# Objectives:
# Practice creating a class and creating new instances
# Practice chaining methods
# Practice writing flexible functions that can take a variable number of arguments
# HINT: To do this exercise, you will probably have to use 'return self'. 
# If the method returns itself (an instance of itself), we can chain methods.

# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x) # should print 5
# which should perform 0+2+(2+5+1)-(3+2) and print 5.


class Math_dojo(object):
    def __init__(self):
        self.result = 0
        
    def subtract(self, arg, *args):
        self.result -= arg 
        for val in args:
            self.result -= val
        return self

    def add(self, arg, *args):
     	self.result += arg
        for val in args:
            self.result += val
        return self



md = Math_dojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

