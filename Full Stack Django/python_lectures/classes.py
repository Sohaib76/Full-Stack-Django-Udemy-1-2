## create a new class

class Square:
    def __init__(self,length):
        self.length = length

    def area(self):
        area = self.length * self.length
        return ("Area: %s" %area)

    def perimeter(self):
        return self.length * 4

    def report(self):
        print("Side Length %s"%self.length)
        print("Area: %s"%self.area())
        print("Parameter: %s" %self.perimeter())



#instantiate class
my_square = Square(20)

print(my_square.report())  #ouput 20


type([])  #output class : list

pass # dont know

def __init__(self):
