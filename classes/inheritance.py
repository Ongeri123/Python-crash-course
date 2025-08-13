class Shape:

    def __init__(self,name,sides):
        self.name = name
        self.sides = sides

    def describe(self):
        print(f"This shape is called {self.name} has {self.sides} sides")


# shape1 = Shape(name ='Circle',sides ='4')
# shape1.describe()

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__('Rectangle', 4 )
        self.width = width
        self.length = length

r1  = Rectangle(length = 10, width = 5)
r1.describe()

